from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from shop.models import Order


@login_required # 로그인 상태일 때만 /profile 페이지로 접근 가능하도록
def profile(request):
    order_list = request.user.order_set.all()
    # order_list = Order.objects.filter(user=request.user)
    return render(request, 'accounts/profile.html', {
        'order_list': order_list,
    })
