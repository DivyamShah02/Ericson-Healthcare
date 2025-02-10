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
                            "user_unauthorized": False,                            
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
                            "user_unauthorized": False,
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
                            "user_unauthorized": False,
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
                            "user_unauthorized": False,                            
                            "data":None,
                            "error": str('Final Report not saved to database')
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_type = case_details.type_of_case

            if case_type == 'Retail Cashless':
                report_data = RetailCashlessFinalReport.objects.filter(id=final_report_id).first()
                report_serializer = RetailCashlessFinalReportSerializers(report_data)

            elif case_type == 'Retail Reimbursement':
                report_data = RetailReimbursementFinalReport.objects.filter(id=final_report_id).first()
                report_serializer = RetailReimbursementFinalReportSerializers(report_data)

            elif case_type == 'Group Cashless':
                report_data = GroupCashlessClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = GroupCashlessClosureReportSerializers(report_data)

            elif case_type == 'Group Reimbursement':
                report_data = GroupReimbursementFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = GroupReimbursementFinalClosureReportSerializers(report_data)

            elif case_type == 'PA Death':
                report_data = PADeathReport.objects.filter(id=final_report_id).first()
                report_serializer = PADeathReportSerializers(report_data)

            elif case_type == 'SMC Death':
                report_data = SecureMindCriticalIllnessDeathFinalReport.objects.filter(id=final_report_id).first()
                report_serializer = SecureMindCriticalIllnessDeathFinalReportSerializers(report_data)

            elif case_type == 'SMC Live':
                report_data = SecureMindCriticalIllnessLiveFinalReport.objects.filter(id=final_report_id).first()
                report_serializer = SecureMindCriticalIllnessLiveFinalReportSerializers(report_data)

            elif case_type == 'PTD':
                report_data = PermanentTotalDisabilityFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = PermanentTotalDisabilityFinalClosureReportSerializers(report_data)

            elif case_type == 'PPD':
                report_data = PermanentPartialDisabilityFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = PermanentPartialDisabilityFinalClosureReportSerializers(report_data)

            elif case_type == 'TTD':
                report_data = TTDReport.objects.filter(id=final_report_id).first()
                report_serializer = TTDReportSerializers(report_data)

            elif case_type == 'PA HDC':
                report_data = PersonalAccidentHDCFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = PersonalAccidentHDCFinalClosureReportSerializers(report_data)

            elif case_type == 'SMC HDC':
                report_data = SecureMindClaimHospitalDailyCashFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = SecureMindClaimHospitalDailyCashFinalClosureReportSerializers(report_data)

            elif case_type == 'LOJ':
                report_data = LossOfJobFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = LossOfJobFinalClosureReportSerializers(report_data)

            elif case_type == 'WC':
                report_data = WorkmanCompensationFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = WorkmanCompensationFinalClosureReportSerializers(report_data)

            elif case_type == 'Broken Bones':
                report_data = BrokenBones.objects.filter(id=final_report_id).first()
                report_serializer = BrokenBonesSerializers(report_data)

            elif case_type == 'HDC':
                report_data = HospitalDailyCashFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = HospitalDailyCashFinalClosureReportSerializers(report_data)

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
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
                            "user_unauthorized": False,                            
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
                            "user_unauthorized": False,                            
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
                            "user_unauthorized": False,
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
                            "user_unauthorized": False,
                            "data":None,
                            "error": f'Case with id - {case_id} not found'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_details = CaseDetails.objects.get(case_id=case_id)
            case_type = case_details.type_of_case
            

            if case_type == 'Retail Cashless':
                report_serializer = RetailCashlessFinalReportSerializers(data=request.data)

            elif case_type == 'Retail Reimbursement':
                report_serializer = RetailReimbursementFinalReportSerializers(data=request.data)

            elif case_type == 'Group Cashless':
                report_serializer = GroupCashlessClosureReportSerializers(data=request.data)

            elif case_type == 'Group Reimbursement':
                report_serializer = GroupReimbursementFinalClosureReportSerializers(data=request.data)

            elif case_type == 'PA Death':
                report_serializer = PADeathReportSerializers(data=request.data)

            elif case_type == 'SMC Death':
                report_serializer = SecureMindCriticalIllnessDeathFinalReportSerializers(data=request.data)

            elif case_type == 'SMC Live':
                report_serializer = SecureMindCriticalIllnessLiveFinalReportSerializers(data=request.data)

            elif case_type == 'PTD':
                report_serializer = PermanentTotalDisabilityFinalClosureReportSerializers(data=request.data)

            elif case_type == 'PPD':
                report_serializer = PermanentPartialDisabilityFinalClosureReportSerializers(data=request.data)

            elif case_type == 'TTD':
                report_serializer = TTDReportSerializers(data=request.data)

            elif case_type == 'PA HDC':
                report_serializer = PersonalAccidentHDCFinalClosureReportSerializers(data=request.data)

            elif case_type == 'SMC HDC':
                report_serializer = SecureMindClaimHospitalDailyCashFinalClosureReportSerializers(data=request.data)

            elif case_type == 'LOJ':
                report_serializer = LossOfJobFinalClosureReportSerializers(data=request.data)

            elif case_type == 'WC':
                report_serializer = WorkmanCompensationFinalClosureReportSerializers(data=request.data)

            elif case_type == 'Broken Bones':
                report_serializer = BrokenBonesSerializers(data=request.data)

            elif case_type == 'HDC':
                report_serializer = HospitalDailyCashFinalClosureReportSerializers(data=request.data)


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
                            "user_unauthorized": False,
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
                            "user_unauthorized": False,                            
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
                            "user_unauthorized": False,                            
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
                            "user_unauthorized": False,                            
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
                            "user_unauthorized": False,
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
                            "user_unauthorized": False,
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
                            "user_unauthorized": False,                            
                            "data":None,
                            "error": str('Final Report not saved to database')
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_type = case_details.type_of_case


            if case_type == 'Retail Cashless':
                report_data = RetailCashlessFinalReport.objects.filter(id=final_report_id).first()
                report_serializer = RetailCashlessFinalReportSerializers(report_data)

            elif case_type == 'Retail Reimbursement':
                report_data = RetailReimbursementFinalReport.objects.filter(id=final_report_id).first()
                report_serializer = RetailReimbursementFinalReportSerializers(report_data)

            elif case_type == 'Group Cashless':
                report_data = GroupCashlessClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = GroupCashlessClosureReportSerializers(report_data)

            elif case_type == 'Group Reimbursement':
                report_data = GroupReimbursementFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = GroupReimbursementFinalClosureReportSerializers(report_data)

            elif case_type == 'PA Death':
                report_data = PADeathReport.objects.filter(id=final_report_id).first()
                report_serializer = PADeathReportSerializers(report_data)

            elif case_type == 'SMC Death':
                report_data = SecureMindCriticalIllnessDeathFinalReport.objects.filter(id=final_report_id).first()
                report_serializer = SecureMindCriticalIllnessDeathFinalReportSerializers(report_data)

            elif case_type == 'SMC Live':
                report_data = SecureMindCriticalIllnessLiveFinalReport.objects.filter(id=final_report_id).first()
                report_serializer = SecureMindCriticalIllnessLiveFinalReportSerializers(report_data)

            elif case_type == 'PTD':
                report_data = PermanentTotalDisabilityFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = PermanentTotalDisabilityFinalClosureReportSerializers(report_data)

            elif case_type == 'PPD':
                report_data = PermanentPartialDisabilityFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = PermanentPartialDisabilityFinalClosureReportSerializers(report_data)

            elif case_type == 'TTD':
                report_data = TTDReport.objects.filter(id=final_report_id).first()
                report_serializer = TTDReportSerializers(report_data)

            elif case_type == 'PA HDC':
                report_data = PersonalAccidentHDCFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = PersonalAccidentHDCFinalClosureReportSerializers(report_data)

            elif case_type == 'SMC HDC':
                report_data = SecureMindClaimHospitalDailyCashFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = SecureMindClaimHospitalDailyCashFinalClosureReportSerializers(report_data)

            elif case_type == 'LOJ':
                report_data = LossOfJobFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = LossOfJobFinalClosureReportSerializers(report_data)

            elif case_type == 'WC':
                report_data = WorkmanCompensationFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = WorkmanCompensationFinalClosureReportSerializers(report_data)

            elif case_type == 'Broken Bones':
                report_data = BrokenBones.objects.filter(id=final_report_id).first()
                report_serializer = BrokenBonesSerializers(report_data)

            elif case_type == 'HDC':
                report_data = HospitalDailyCashFinalClosureReport.objects.filter(id=final_report_id).first()
                report_serializer = HospitalDailyCashFinalClosureReportSerializers(report_data)

            report_data = report_serializer.data

            pdf_buffer = create_pdf_from_dict(data_dict=report_data, case_type=case_type, case_id=case_id)
            
            pdf_response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
            pdf_response['Content-Disposition'] = 'inline; filename="FinalReport.pdf"'

            # Reset buffer position before returning it
            pdf_buffer.close()

            return pdf_response
            
            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
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
                            "user_unauthorized": False,                            
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

