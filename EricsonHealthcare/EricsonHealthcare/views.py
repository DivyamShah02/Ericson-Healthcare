from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from UserRole.models import UserDetail
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse

from Visit.models import City
from Case.models import Case

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

def test_api(request):
    all_cases = Case.objects.all()
    for case_data in all_cases:
        document_paths = case_data.document_paths
        new_document_paths = []
        for path in document_paths:
            if 'https://ehunt.s3.eu-north-1.amazonaws.com/' not in path:
                new_path = 'https://ehunt.s3.eu-north-1.amazonaws.com/' + path
                new_document_paths.append(new_path)
            print(path)
        case_obj = Case.objects.get(case_id=case_data.case_id)
        case_obj.document_paths = new_document_paths
        case_obj.save()
    return HttpResponse('done')
