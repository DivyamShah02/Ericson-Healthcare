from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from UserRole.models import UserDetail
from django.http import HttpResponseBadRequest

def login_to_account(request):
    try:
        request_user = request.user
        username = request.GET.get('username')
        print(username)

        user = UserDetail.objects.get(username=username)

        if request_user.is_staff:
            print('Staff')
            login(request, user)

        return redirect('dashboard-list')

    except Exception as e:
        print(e)
        return redirect('dashboard-list')
