from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required # 로그인 상태일 때만 /profile 페이지로 접근 가능하도록
def profile(request):
    return render(request, 'accounts/profile.html')
