from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from UserRole.models import UserDetail
from django.http import HttpResponseBadRequest, JsonResponse

from Visit.models import City

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

def add_city(request):
    try:
            city = request.GET.get('city')
            state = request.GET.get('state')
            print(city, state)
            city_obj = City.objects.create(city=city, state=state)
            city_obj.save()
            return JsonResponse({'status': 'success', 'message': 'City added successfully'})

    except Exception as e:
        print(e)
        return JsonResponse({'status': 'failed', 'message': 'City not added'})
