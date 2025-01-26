from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, ParseError
from django.shortcuts import get_object_or_404, render, redirect

from Case.models import Case, CaseDetails


class LoginViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'login.html')

class UserRegisterViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, "user_registration.html")

class DashboardViewSet(viewsets.ViewSet):
    def list(self, request):
        if request.user.is_staff:
            return render(request, 'Admin/dashboard.html')
            return redirect('register-list')
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
            case_details_data = CaseDetails.objects.filter(case_id=case_id).first()

            if case_details is None:
                print(f'Wrong case id | No case with id {case_id} present')
                return redirect('dashboard-list')

            if user_role == 'hod':
                if case_details.case_status == 'Creation' or case_details.case_status == 'Creation_confirmation':
                    return render(request, 'Hod/case_overview.html')

                elif case_details.case_status == 'Investigation' or case_details.case_status == 'Investigation_confirmation':
                    return render(request, 'Hod/investigation.html')

                elif case_details.case_status == 'Medical' or case_details.case_status == 'Medical_confirmation':
                    return render(request, 'Hod/medical_remark.html')

                elif case_details.case_status == 'Data_entry' or case_details.case_status == 'Data_entry_confirmation':
                    return render(request, 'Hod/data_entry.html')

                elif case_details.case_status == 'Final_report' or case_details.case_status == 'Final_report_confirmation':
                    return render(request, 'Hod/final_report_submit.html')

                elif case_details.case_status == 'Complete':
                    return render(request, 'Hod/case_completed.html')

                return redirect('dashboard-list')

            elif user_role == 'coordinator':
                if case_details.case_status == 'Creation' or case_details.case_status == 'Creation_confirmation':
                    return render(request, 'Coordinator/case_overview.html')

                elif case_details.case_status == 'Investigation' or case_details.case_status == 'Investigation_confirmation':
                    return render(request, 'Coordinator/investigation.html')

                elif case_details.case_status == 'Medical' or case_details.case_status == 'Medical_confirmation':
                    return render(request, 'Coordinator/medical_remark.html')

                elif case_details.case_status == 'Data_entry' or case_details.case_status == 'Data_entry_confirmation':
                    return render(request, 'Coordinator/data_entry.html')

                elif case_details.case_status == 'Final_report' or case_details.case_status == 'Final_report_confirmation':
                    return render(request, 'Coordinator/final_report_submit.html')

                elif case_details.case_status == 'Complete':
                    return render(request, 'Coordinator/case_completed.html')

            elif user_role == 'investigator':
                if case_details.case_status == 'Investigation':
                    return render(request, 'Investigate Officer/investigation.html')
                
                elif case_details.case_status == 'Investigation_confirmation' or\
                    case_details.case_status == 'Medical' or case_details.case_status == 'Medical_confirmation' or\
                    case_details.case_status == 'Data_entry' or case_details.case_status == 'Data_entry_confirmation' or\
                    case_details.case_status == 'Final_report' or case_details.case_status == 'Final_report_confirmation' or\
                    case_details.case_status == 'Complete':
                    
                    return render(request, 'Investigate Officer/case_completed.html')
                
                else:
                    return redirect('dashboard-list')

            elif user_role == 'medical_officer':
                if case_details.case_status == 'Medical':
                    return render(request, 'Medical Officer/medical_remark.html')
                
                elif case_details.case_status == 'Medical_confirmation' or\
                    case_details.case_status == 'Data_entry' or case_details.case_status == 'Data_entry_confirmation' or\
                    case_details.case_status == 'Final_report' or case_details.case_status == 'Final_report_confirmation' or\
                    case_details.case_status == 'Complete':
                    
                    return render(request, 'Medical Officer/case_completed.html')

                else:
                    return redirect('dashboard-list')

            elif user_role == 'data_entry_personnel':
                if case_details.case_status == 'Data_entry':
                    case_type = case_details_data.type_of_case
                    print(case_type)
                    return render(request, 'DataEntry/data_entry.html', {'case_type':case_type})
                
                elif case_details.case_status == 'Data_entry_confirmation' or\
                    case_details.case_status == 'Final_report' or case_details.case_status == 'Final_report_confirmation' or\
                    case_details.case_status == 'Complete':
                    
                    return render(request, 'DataEntry/case_completed.html')

                else:
                    return redirect('dashboard-list')

            elif user_role == 'admin':
                return redirect('dashboard-list')
        
        except Exception as ex:
            # logger.error(ex, exc_info=True)
            print(ex)
            return redirect('dashboard-list')

class ReportViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            user = request.user

            if not user.is_authenticated:
                return redirect('login-list')

            user_role = user.role
            print(user_role)

            if user_role == 'hod':
                return render(request, 'Hod/report.html')

            elif user_role == 'coordinator':
                return render(request, 'Coordinator/report.html')

            elif user_role == 'investigator':
                return render(request, 'Investigate Officer/report.html')

            elif user_role == 'medical_officer':
                return render(request, 'Medical Officer/report.html')

            elif user_role == 'data_entry_personnel':
                return render(request, 'DataEntry/report.html')

            elif user_role == 'admin':
                return render(request, 'Admin/report.html')

        except Exception as ex:
            # logger.error(ex, exc_info=True)
            print(ex)
            return redirect('dashboard-list')

class QuestionAdderViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            user = request.user

            if not user.is_authenticated:
                return redirect('login-list')

            user_role = user.role
            print(user_role)

            if user_role == 'admin' or user_role == 'hod' or user_role == 'coordinator' or user_role == 'medical_officer':
                return render(request, 'question_adder.html')

            return redirect('dashboard-list')

        except Exception as ex:
            # logger.error(ex, exc_info=True)
            print(ex)
            return redirect('dashboard-list')

class PrivacyPolicyViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'privacy_policy.html')
