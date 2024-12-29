import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *
from Case.models import Case, CaseDetails

from .Final_Report import create_pdf_from_dict


class AddFinalReportViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            user = request.user
            if not user.is_authenticated:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": True,
                            "user_unathorized": False,                            
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_id = request.GET.get('case_id')
            if not case_id:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "data":None,
                            "error": '"case_id" is required'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_data = Case.objects.get(case_id=case_id)
            if case_data is None:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "data":None,
                            "error": f'Case with id - {case_id} not found'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_details = CaseDetails.objects.get(case_id=case_id)
            
            final_report_id = case_details.final_report
            if final_report_id == '':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,                            
                            "data":None,
                            "error": str('Final Report not saved to database')
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_type = case_details.type_of_case

            if case_type == 'CashlessClaimReport':
                report_data = CashlessClaimReport.objects.filter(id=final_report_id).first()
                report_serializer = CashlessClaimReportSerializers(report_data)

            elif case_type == 'ClaimReport':
                report_data = ClaimReport.objects.filter(id=final_report_id).first()
                report_serializer = ClaimReportSerializers(report_data)

            elif case_type == 'HDCClosureReport':
                report_data = HDCClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = HDCClosureReportSerializers(report_data)

            elif case_type == 'HealthClaimReport':
                report_data = HealthClaimReport.objects.filter(id=final_report_id).first()
                report_serializer = HealthClaimReportSerializers(report_data)

            elif case_type == 'ICLMClosureReport':
                report_data = ICLMClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = ICLMClosureReportSerializers(report_data)

            elif case_type == 'PADeathReport':
                report_data = PADeathReport.objects.filter(id=final_report_id).first()
                report_serializer = PADeathReportSerializers(report_data)

            elif case_type == 'SecureMindCriticalIllnessReport':
                report_data = SecureMindCriticalIllnessReport.objects.filter(id=final_report_id).first()
                report_serializer = SecureMindCriticalIllnessReportSerializers(report_data)

            elif case_type == 'TTDReport':
                report_data = TTDReport.objects.filter(id=final_report_id).first()
                report_serializer = TTDReportSerializers(report_data)

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "data":report_serializer.data,
                        "error": None
                    },
                    status=status.HTTP_200_OK
                )

        except Exception as ex:
            # logger.error(ex, exc_info=True)
            return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,                            
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

    def create(self, request):
        try:
            user = request.user
            if not user.is_authenticated:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": True,
                            "user_unathorized": False,                            
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_id = request.data.get('case_id')
            if not case_id:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "data":None,
                            "error": '"case_id" is required'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_data = Case.objects.get(case_id=case_id)
            if case_data is None:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "data":None,
                            "error": f'Case with id - {case_id} not found'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_details = CaseDetails.objects.get(case_id=case_id)
            case_type = case_details.type_of_case
            
            if case_type == 'CashlessClaimReport':
                report_serializer = CashlessClaimReportSerializers(data=request.data)
            elif case_type == 'ClaimReport':
                report_serializer = ClaimReportSerializers(data=request.data)
            elif case_type == 'HDCClosureReport':
                report_serializer = HDCClosureReportSerializers(data=request.data)
            elif case_type == 'HealthClaimReport':
                report_serializer = HealthClaimReportSerializers(data=request.data)
            elif case_type == 'ICLMClosureReport':
                report_serializer = ICLMClosureReportSerializers(data=request.data)
            elif case_type == 'PADeathReport':
                report_serializer = PADeathReportSerializers(data=request.data)
            elif case_type == 'SecureMindCriticalIllnessReport':
                report_serializer = SecureMindCriticalIllnessReportSerializers(data=request.data)
            elif case_type == 'TTDReport':
                report_serializer = TTDReportSerializers(data=request.data)
            
            if report_serializer.is_valid():
                save_report_serializer = report_serializer.save()
                print(report_serializer.data)

                case_details.final_report = save_report_serializer.id

                case_details.save()
                case_data.save()

                return Response(
                        {
                            "success": True,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "data":report_serializer.data,
                            "error": None
                        },
                        status=status.HTTP_200_OK
                    )

            else:
                # logger.error(report_serializer.data)
                print(report_serializer.errors)
                print('________________________________')
                print(report_serializer.error_messages)

                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,                            
                            "data":None,
                            "error": report_serializer.errors
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )


        except Exception as ex:
            # logger.error(ex, exc_info=True)
            return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,                            
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )


class RenderFinalReportViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            user = request.user
            if not user.is_authenticated:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": True,
                            "user_unathorized": False,                            
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_id = request.GET.get('case_id')
            if not case_id:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "data":None,
                            "error": '"case_id" is required'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_data = Case.objects.get(case_id=case_id)
            if case_data is None:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "data":None,
                            "error": f'Case with id - {case_id} not found'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_details = CaseDetails.objects.get(case_id=case_id)
            
            final_report_id = case_details.final_report
            if final_report_id == '':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,                            
                            "data":None,
                            "error": str('Final Report not saved to database')
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_type = case_details.type_of_case

            if case_type == 'CashlessClaimReport':
                report_data = CashlessClaimReport.objects.filter(id=final_report_id).first()
                report_serializer = CashlessClaimReportSerializers(report_data)

            elif case_type == 'ClaimReport':
                report_data = ClaimReport.objects.filter(id=final_report_id).first()
                report_serializer = ClaimReportSerializers(report_data)

            elif case_type == 'HDCClosureReport':
                report_data = HDCClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = HDCClosureReportSerializers(report_data)

            elif case_type == 'HealthClaimReport':
                report_data = HealthClaimReport.objects.filter(id=final_report_id).first()
                report_serializer = HealthClaimReportSerializers(report_data)

            elif case_type == 'ICLMClosureReport':
                report_data = ICLMClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = ICLMClosureReportSerializers(report_data)

            elif case_type == 'PADeathReport':
                report_data = PADeathReport.objects.filter(id=final_report_id).first()
                report_serializer = PADeathReportSerializers(report_data)

            elif case_type == 'SecureMindCriticalIllnessReport':
                report_data = SecureMindCriticalIllnessReport.objects.filter(id=final_report_id).first()
                report_serializer = SecureMindCriticalIllnessReportSerializers(report_data)

            elif case_type == 'TTDReport':
                report_data = TTDReport.objects.filter(id=final_report_id).first()
                report_serializer = TTDReportSerializers(report_data)

            report_data = report_serializer.data

            pdf_buffer = create_pdf_from_dict(data_dict=report_data, case_type=case_type, case_id=case_id)
            
            pdf_response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
            pdf_response['Content-Disposition'] = 'inline; filename="visit_plan.pdf"'

            # Reset buffer position before returning it
            pdf_buffer.close()

            return pdf_response
            
            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "data":report_serializer.data,
                        "error": None
                    },
                    status=status.HTTP_200_OK
                )

        except Exception as ex:
            # logger.error(ex, exc_info=True)
            return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,                            
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

