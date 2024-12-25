from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, ParseError
from django.shortcuts import get_object_or_404, render, redirect

from Case.models import Case, CaseDetails


class LoginViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'login.html')

class DashboardViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'dashboard.html')

class CaseOverviewViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            user = request.user

            if not user.is_authenticated:
                return redirect('login-list')

            user_role = user.role
            case_id = request.GET.get('case_id')
            print(user_role)

            if not case_id:
                print(f'Case Id not present')
                return redirect('dashboard-list')

            case_details = Case.objects.filter(case_id=case_id).first()

            if case_details is None:
                print(f'Wrong case id | No case with id {case_id} present')
                return redirect('dashboard-list')

            if user_role == 'hod':
                pass

            elif user_role == 'coordinator':
                if case_details.case_status == 'Creation' or case_details.case_status == 'Creation_confirmation':
                    return render(request, 'Coordinator/case_overview.html')

                elif case_details.case_status == 'Investigation' or case_details.case_status == 'Investigation_confirmation':
                    return render(request, 'Coordinator/investigation.html')

                elif case_details.case_status == 'Medical' or case_details.case_status == 'Medical_confirmation':
                    return render(request, 'Coordinator/medical_remark.html')

                elif case_details.case_status == 'Data_entry' or case_details.case_status == 'Data_entry_confirmation':
                    return render(request, 'Coordinator/data_entry.html')

            elif user_role == 'investigator':
                pass
            elif user_role == 'medical_officer':
                pass
            elif user_role == 'data_entry_personnel':
                pass
            elif user_role == 'admin':
                pass
        
        except Exception as ex:
            # logger.error(ex, exc_info=True)
            print(ex)
            return redirect('dashboard-list')
