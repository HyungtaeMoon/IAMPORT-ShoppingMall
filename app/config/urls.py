from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', lambda request: redirect('shop:index'), name='root')
]
