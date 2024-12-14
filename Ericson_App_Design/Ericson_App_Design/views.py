from django.shortcuts import render, redirect, HttpResponse

def home(request):
    data = {
        'urls':[
            'login',
            'Coordinator_dashboard',
            'Coordinator_case_overview',
            'Coordinator_investigation',
            'Coordinator_medical_remark',
            'Coordinator_data_entry',
            'Coordinator_final_report_submit',
            'Coordinator_case_completed',
            'Investigate_Officer_dashboard',
            'Investigate_Officer_investigation',
            'Medical_Officer_dashboard',
            'Medical_Officer_medical_remark',
        ]
    }

    return render(request, 'index.html', data)
def login_page(request):
    return render(request, 'login.html')
def Coordinator_dashboard(request):
    return render(request, 'Case view - Coordinator/dashboard.html')
def Coordinator_case_overview(request):
    return render(request, 'Case view - Coordinator/case_overview.html')
def Coordinator_investigation(request):
    return render(request, 'Case view - Coordinator/investigation.html')
def Coordinator_medical_remark(request):
    return render(request, 'Case view - Coordinator/medical_remark.html')
def Coordinator_data_entry(request):
    return render(request, 'Case view - Coordinator/data_entry.html')
def Coordinator_final_report_submit(request):
    return render(request, 'Case view - Coordinator/final_report_submit.html')
def Coordinator_case_completed(request):
    return render(request, 'Case view - Coordinator/case_completed.html')
def Investigate_Officer_dashboard(request):
    return render(request, 'Case view - Investigate Officer/dashboard.html')
def Investigate_Officer_investigation(request):
    return render(request, 'Case view - Investigate Officer/investigation.html')
def Medical_Officer_dashboard(request):
    return render(request, 'Case view - Medical Officer/dashboard.html')
def Medical_Officer_medical_remark(request):
    return render(request, 'Case view - Medical Officer/medical_remark.html')


# Ericson_App_Design/templates/Case view - Coordinator 
# Ericson_App_Design/templates/Case view - Coordinator/case_completed.html 
# Ericson_App_Design/templates/Case view - Coordinator/case_overview.html 
# Ericson_App_Design/templates/Case view - Coordinator/Coordinator-flow.png 
# Ericson_App_Design/templates/Case view - Coordinator/dashboard.html 
# Ericson_App_Design/templates/Case view - Coordinator/data_entry.html 
# Ericson_App_Design/templates/Case view - Coordinator/final_report_submit.html 
# Ericson_App_Design/templates/Case view - Coordinator/investigation.html 
# Ericson_App_Design/templates/Case view - Coordinator/medical_remark.html 
# Ericson_App_Design/templates/Case view - Investigate Officer 
# Ericson_App_Design/templates/Case view - Investigate Officer/dashboard.html 
# Ericson_App_Design/templates/Case view - Investigate Officer/investigation.html 
# Ericson_App_Design/templates/Case view - Medical Officer 
# Ericson_App_Design/templates/Case view - Medical Officer/dashboard.html 
# Ericson_App_Design/templates/Case view - Medical Officer/medical_remark.html

