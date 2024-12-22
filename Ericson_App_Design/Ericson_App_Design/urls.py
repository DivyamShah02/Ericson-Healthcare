from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('Coordinator_dashboard/', Coordinator_dashboard, name='Coordinator_dashboard'),
    path('Coordinator_case_overview/', Coordinator_case_overview, name='Coordinator_case_overview'),
    path('Coordinator_investigation/', Coordinator_investigation, name='Coordinator_investigation'),
    path('Coordinator_medical_remark/', Coordinator_medical_remark, name='Coordinator_medical_remark'),
    path('Coordinator_data_entry/', Coordinator_data_entry, name='Coordinator_data_entry'),
    path('Coordinator_final_report_submit/', Coordinator_final_report_submit, name='Coordinator_final_report_submit'),
    path('Coordinator_case_completed/', Coordinator_case_completed, name='Coordinator_case_completed'),
    path('Investigate_Officer_dashboard/', Investigate_Officer_dashboard, name='Investigate_Officer_dashboard'),
    path('Investigate_Officer_investigation/', Investigate_Officer_investigation, name='Investigate_Officer_investigation'),
    path('Medical_Officer_dashboard/', Medical_Officer_dashboard, name='Medical_Officer_dashboard'),
    path('Medical_Officer_medical_remark/', Medical_Officer_medical_remark, name='Medical_Officer_medical_remark'),
]
