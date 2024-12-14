import os

from django.conf import settings
from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Case, CaseDetails
from .serializers import CaseSerializers, CaseDetailsSerializer

logger = None

class CaseViewSet_old(viewsets.ViewSet):
    
    def create(self, request):
        serializer = CaseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        """
        This view returns a list of cases associated with the current logged-in user.
        """
        
        user = self.request.user
        user = 'hod_id'
        print("===============", request, self.request.user)

        if hasattr(user, 'coordinator_id'):
            cases = Case.objects.filter(coordinator_id=user.coordinator_id)
        elif hasattr(user, 'hod_id'):
            cases = Case.objects.filter(hod_id=user.hod_id)
        elif hasattr(user, 'medical_officer_id'):
            cases = Case.objects.filter(medical_officer_id=user.medical_officer_id)
        elif hasattr(user, 'data_entry_id'):
            cases = Case.objects.filter(data_entry_id=user.data_entry_id)
        else:
            cases = Case.objects.none()

        serializer = CaseSerializers(cases, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'], url_path='update-medical-officer-remarks')
    def update_medical_officer_remarks(self, request):
        # Retrieve case_id and medical_officer_remarks from request data
        case_id = request.data.get('case_id')
        medical_officer_remarks = request.data.get('medical_officer_remarks')

        # Check if both case_id and medical_officer_remarks are provided
        if not case_id or not medical_officer_remarks:
            return Response({"error": "Both case_id and medical_officer_remarks are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch the CaseDetails object using the case_id
            case_detail = CaseDetails.objects.get(case_id=case_id)

            # Update the medical_officer_remarks field
            case_detail.medical_officer_remarks = medical_officer_remarks
            case_detail.save()

            # Serialize the updated CaseDetails object
            serializer = CaseDetailsSerializer(case_detail)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except CaseDetails.DoesNotExist:
            return Response({"error": f"Case with id {case_id} not found."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['post'], url_path='get-cases-by-medical-officer')
    def get_case_details_by_medical_officer(self, request):
        medical_officer_id = request.data.get('medical_officer_id')

        if not medical_officer_id:
            return Response({"error": "medical_officer_id is required."}, 
                            status=status.HTTP_400_BAD_REQUEST)
    
        try:
            medical_officer_cases = Case.objects.filter(medical_officer_id=medical_officer_id)
            case_serializer = CaseSerializers(medical_officer_cases, many=True)
            case_serializer = case_serializer.data

            return Response(case_serializer, status=status.HTTP_200_OK)
        
        except Exception as ex:
            return Response({"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @action(detail=False, methods=['post'], url_path='get-case-visit-details-by-case-id')
    def get_case_and_visit_details_by_case_id(self, request):
        case_id = request.data.get('case_id')

        if not case_id:
            return Response({"error": "case_id is required."}, 
                            status=status.HTTP_400_BAD_REQUEST)

class CaseDetailsViewSet_old(viewsets.ViewSet):
    
    def create(self, request):
        serializer = CaseDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['post'], url_path='by-caseid')
    def get_case_details_by_case_id(self, request, case_id=None):
        try:
            case_id = request.data.get('case_id')
            print("csaseda ", case_id)

            if not case_id:
                return Response({"error": "case_id is required."}, status=status.HTTP_400_BAD_REQUEST)

            # Filter CaseDetails by case_id
            case_details = CaseDetails.objects.filter(case_id=case_id)
            print("125235 ", case_details)
            serializer = CaseDetailsSerializer(case_details, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], url_path='update-medical-officer')
    def update_medical_officer(self, request):
        # Extract case_id and medical_officer_id from request
        case_id = request.data.get('case_id')
        medical_officer_id = request.data.get('medical_officer_id')

        # Validate that both fields are provided
        if not case_id or not medical_officer_id:
            return Response({"error": "Both 'case_id' and 'medical_officer_id' are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch the Case instance using case_id
            case_instance = Case.objects.get(case_id=case_id)

            # Update the medical_officer_id field
            case_instance.medical_officer_id = medical_officer_id
            case_instance.save()  # Save the changes to the database

            # Return the updated case instance in response
            serializer = CaseSerializers(case_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Case.DoesNotExist:
            return Response({"error": f"Case with ID {case_id} not found."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CaseDetailsViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            user = request.user

            if not user.is_authenticated:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": True,
                            "case_details_not_added": False,
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
                            "case_details_not_added": False,
                            "data":None,
                            "error": '"case_id" is required'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_details_obj = CaseDetails.objects.filter(case_id=case_id).first()

            if case_details_obj is None:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "case_details_not_added": True,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_details = CaseDetailsSerializer(case_details_obj).data

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "case_details_not_added": False,
                        "data":case_details,
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
                        "case_details_not_added": False,
                        "data":None,
                        "error": str(ex)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
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

            user_role = user.role

            if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": True,
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

            case_data = Case.objects.filter(case_id=case_id).first()

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

            case_details_obj = CaseDetails.objects.filter(case_id=case_id).first()

            if case_details_obj is None:
                case_obj = CaseDetails(case_id=case_id)
            
            else:
                case_obj = CaseDetails.objects.get(case_id=case_id)
            
            case_obj.coordinator_id = case_data.coordinator_id

            case_obj.claim_number = request.data.get('claim_number')
            case_obj.doa = request.data.get('doa')
            case_obj.dod = request.data.get('dod')
            case_obj.hospital_name = request.data.get('hospital_name')
            case_obj.city = request.data.get('city')
            case_obj.state = request.data.get('state')
            case_obj.claim_value = request.data.get('claim_value')
            case_obj.diagnosis = request.data.get('diagnosis')

            case_obj.save()

            updated_case_details_obj = CaseDetails.objects.filter(case_id=case_id).first()
            update_case_details = CaseDetailsSerializer(updated_case_details_obj).data
            
            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "data":update_case_details,
                        "error": None
                    },
                    status=status.HTTP_200_OK
                )

        except Exception as ex:
            # logger.error(ex, exc_info=True)
            print(ex)
            return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "data":None,
                        "error": str(ex)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

class CaseViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            user = request.user

            if not user.is_authenticated:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": True,
                            "user_unathorized": False,
                            "file_not_attached": False,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            user_role = user.role

            if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": True,
                            "file_not_attached": False,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )


            if 'file' not in request.FILES:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "file_not_attached": True,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            coordinator_id = request.data.get('coordinator_id')

            uploaded_file = request.FILES['file']
            file_path = self.save_file(uploaded_file)

            try:
                last_case = Case.objects.latest('id')
                case_id = int(last_case.case_id) + 1
            
            except Case.DoesNotExist:
                case_id = 1000
            
            new_case = Case(case_id=case_id)
            new_case.document_paths = [f"{file_path}"]
            
            if user_role == 'hod':
                new_case.hod_id = user
                if coordinator_id:
                    new_case.coordinator_id = coordinator_id

            elif user_role == 'coordinator':
                new_case.coordinator_id = user

            new_case.save()

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "file_not_attached": False,
                        "data":{'case_id':case_id},
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
                            "file_not_attached": False,
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

    def list(self, request):
        try:
            user = request.user

            if not user.is_authenticated:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": True,
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
                            "data":None,
                            "error": '"case_id" is required'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_obj = Case.objects.filter(case_id=case_id).first()

            if case_obj is None:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "data":None,
                            "error": f'Case with id - {case_id} not found'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_data = CaseSerializers(case_obj).data
            
            docs_path_lst = case_data.get('document_paths')

            all_docs = []
            for doc in docs_path_lst:
                all_docs.append({
                    "path": str(doc),
                    "name": os.path.basename(str(doc))
                })

            case_data['all_docs'] = all_docs

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "data":case_data,
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
                        "data":None,
                        "error": str(ex)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    def save_file(self, uploaded_file):
        # Define the base directory to save the files
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads/')
        os.makedirs(upload_dir, exist_ok=True)

        # Generate a unique filename if a file with the same name exists
        base_name, extension = os.path.splitext(uploaded_file.name)
        file_name = uploaded_file.name
        counter = 1

        while os.path.exists(os.path.join(upload_dir, file_name)):
            file_name = f"{base_name}({counter}){extension}"
            counter += 1

        # Save the file
        file_path = os.path.join(upload_dir, file_name)
        with open(file_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        # Return the relative file path
        return os.path.relpath(file_path, settings.MEDIA_ROOT)

class GetAllCaseViewSet(viewsets.ViewSet):
    def list(self, request):
        """
        This view returns a list of cases associated with the current logged-in user.
        """
        try:
            user = request.user

            if not user.is_authenticated:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": True,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            user_role = user.role

            if user_role == 'hod':
                cases = Case.objects.filter(hod_id=user)

            elif user_role == 'coordinator':
                cases = Case.objects.filter(coordinator_id=user)

            elif user_role == 'investigator':
                pass

            elif user_role == 'medical_officer':
                cases = Case.objects.filter(medical_officer_id=user)

            elif user_role == 'data_entry_personnel':
                cases = Case.objects.filter(data_entry_id=user)

            elif user_role == 'admin':
                pass

            case_data = CaseSerializers(cases, many=True).data

            total_cases = len(case_data)
            in_progress_case_data = [case_obj for case_obj in case_data if case_obj['case_status'] != 'Complete']
            recent_cases = in_progress_case_data[0:5]
            in_progress_cases = len([case_obj for case_obj in case_data if case_obj['case_status'] != 'Complete' and case_obj['case_status'] != 'Creation'])
            closed_cases = len([case_obj for case_obj in case_data if case_obj['case_status'] == 'Complete'])
            pending_cases = len([case_obj for case_obj in case_data if case_obj['case_status'] == 'Creation'])

            data = {
                'total_cases': total_cases,
                'in_progress_cases': in_progress_cases,
                'closed_cases': closed_cases,
                'pending_cases': pending_cases,
                'case_data': case_data,
                'recent_cases': recent_cases
            }

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "data":data,
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
                        "data":None,
                        "error": str(ex)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

