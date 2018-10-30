from uuid import uuid4

from django.conf import settings
from django.db import models
from iamport import Iamport
from jsonfield import JSONField


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    amount = models.PositiveIntegerField()
    photo = models.ImageField()
    is_public = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    item = models.ForeignKey(Item)
    merchant_uid = models.UUIDField(default=uuid4, editable=False)
    imp_uid = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, verbose_name='상품명')
    amount = models.PositiveIntegerField(verbose_name='결제금액')
    status = models.CharField(
        max_length=9,
        choices=(
            ('ready',     '미결제'),
            ('paid',      '결제완료'),
            ('cancelled', '결제취소'),
            ('failed',    '결제실패'),
        ),
        default='ready',
        db_index=True)
    meta = JSONField(blank=True, default={})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ['-id']
        ordering = ('-id',)

    @property
    def api(self):
        return Iamport(settings.IAMPORT_API_KEY, settings.IAMPORT_API_SECRET)

    def update(self, commit=True, meta=None):
        if self.imp_uid:
            self.meta = meta or self.api.find(imp_uid=self.imp_uid)
            # merchant_uid 는 반드시 매칭
            assert str(self.merchant_uid) == self.meta['merchant_uid']
        if commit:
            self.save()
