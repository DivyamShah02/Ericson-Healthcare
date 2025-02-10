import os
import boto3
import base64
from botocore.exceptions import NoCredentialsError

from django.conf import settings
from django.shortcuts import render
from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Case, CaseDetails, InsuranceCompany
from .serializers import CaseSerializers, CaseDetailsSerializer, InsuranceCompanySerializer
from Visit.models import Visit, City
from UserRole.models import UserDetail

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
                            "success": True,
                            "user_not_logged_in": False,
                            "case_details_not_added": True,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_200_OK
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
                            "user_unauthorized": False,
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
                            "user_unauthorized": True,
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

            case_details_obj = CaseDetails.objects.filter(case_id=case_id).first()

            if case_details_obj is None:
                case_obj = CaseDetails(case_id=case_id)
            
            else:
                case_obj = CaseDetails.objects.get(case_id=case_id)
            
            case_obj.coordinator_id = case_data.coordinator_id

            case_obj.claim_number = request.data.get('claim_number')
            case_obj.insurance_company = request.data.get('insurance_company')
            case_obj.type_of_case = request.data.get('type_of_case')
            case_obj.doa = request.data.get('doa')
            case_obj.dod = request.data.get('dod')
            case_obj.hospital_name = request.data.get('hospital_name')
            case_obj.city = request.data.get('city')
            case_obj.state = request.data.get('state')
            case_obj.claim_value = request.data.get('claim_value')
            case_obj.diagnosis = request.data.get('diagnosis')
            case_obj.insured_name = request.data.get('insured_name')
            case_obj.insured_number = request.data.get('insured_number')
            case_obj.insured_address = request.data.get('insured_address')
            case_obj.save()
            
            case_data.case_status = 'Creation_confirmation'
            case_data.claim_number = request.data.get('claim_number')
            case_data.save()

            updated_case_details_obj = CaseDetails.objects.filter(case_id=case_id).first()
            update_case_details = CaseDetailsSerializer(updated_case_details_obj).data
            
            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
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
                        "user_unauthorized": False,
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
                            "user_unauthorized": False,
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
                            "user_unauthorized": True,
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
                            "user_unauthorized": False,
                            "file_not_attached": True,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            coordinator_id = request.data.get('coordinator_id')

            uploaded_file = request.FILES['file']
            # file_path = self.save_file(uploaded_file)
            file_path = self.upload_file_to_s3(uploaded_file)

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
                        "user_unauthorized": False,
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
                            "user_unauthorized": False,
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
                    # "path": os.path.normpath(os.path.join(settings.MEDIA_URL, doc)).replace(os.sep, '/'),
                    "path": os.path.normpath(os.path.join(doc)).replace(os.sep, '/'),
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

    def upload_file_to_s3(self, uploaded_file):
        """Uploads a file to AWS S3, renaming it if a file with the same name exists."""
        region_name = "eu-north-1"
        s3_client = boto3.client(
            "s3",
            aws_access_key_id = self.decrypt("QUtJQTRUNE9DTTU2TENMUUdTNlA="),
            aws_secret_access_key = self.decrypt("TzRzQmlWK0NvcWdBM2Q1aGhPMXJkeGV0c1YyaWdibjR6YXhrbTRqMA=="),
            region_name = region_name
        )
        
        bucket_name = "ehunt"
        base_name, extension = os.path.splitext(uploaded_file.name)
        file_name = uploaded_file.name
        s3_key = f"uploads/{file_name}"
        counter = 1

        # Check if file exists and rename if necessary
        while True:
            try:
                s3_client.head_object(Bucket=bucket_name, Key=s3_key)
                # If file exists, update the filename
                file_name = f"{base_name}({counter}){extension}"
                s3_key = f"uploads/{file_name}"
                counter += 1
            except s3_client.exceptions.ClientError:
                break  # File does not exist, proceed with upload

        # Upload file
        s3_client.upload_fileobj(uploaded_file, bucket_name, s3_key)

        # Generate file URL
        file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{s3_key}"

        return file_url

    def decrypt(self, b64_text):
        # Decode the Base64 string back to bytes, then to text
        return base64.b64decode(b64_text.encode()).decode()


class GetAllCaseViewSet(viewsets.ViewSet):
    def list(self, request):
        """
        This view returns a list of cases associated with the current logged-in user.
        """
        try:
            user = request.user

            case_statuses = ['Creation', 'Creation_confirmation', 'Investigation', 'Investigation_confirmation', 'Medical', 'Medical_confirmation', 'Data_entry', 'Data_entry_confirmation', 'Final_report', 'Final_report_confirmation', 'Complete']

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
            
            custom_user = request.GET.get('custom_user')
            if custom_user:
                user = UserDetail.objects.filter(user_id=custom_user).first()

            user_role = user.role
            if user_role == 'hod':
                cases = Case.objects.filter(hod_id=user)

            elif user_role == 'coordinator':
                cases = Case.objects.filter(coordinator_id=user)

            elif user_role == 'investigator':
                all_visits = Visit.objects.filter(investigator_id=user)

                visit_cases = [visit_details.case_id for visit_details in all_visits]
                visit_cases = list(set(visit_cases))
                
                cases = Case.objects.filter(case_id__in=visit_cases)
                investigation_case_status = case_statuses[2:len(case_statuses)]
                cases = [case for case in cases if case.case_status in investigation_case_status]

            elif user_role == 'medical_officer':
                cases = Case.objects.filter(medical_officer_id=user)
                medical_case_status = case_statuses[4:len(case_statuses)]
                cases = [case for case in cases if case.case_status in medical_case_status]

            elif user_role == 'data_entry_personnel':
                cases = Case.objects.filter(data_entry_id=user)
                data_entry_case_status = case_statuses[6:len(case_statuses)]
                cases = [case for case in cases if case.case_status in data_entry_case_status]

            elif user_role == 'admin':
                pass
            
            cases = cases[::-1]
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

class AddDocumentViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            user = request.user

            if not user.is_authenticated:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": True,
                            "user_unauthorized": False,
                            "file_not_attached": False,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            user_role = user.role

            if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin' and user_role != 'investigator':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": True,
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
                            "user_unauthorized": False,
                            "file_not_attached": True,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            case_id = request.data.get('case_id')
            case_data = Case.objects.get(case_id=case_id)
            if not case_data:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,
                            "file_not_attached": False,
                            "data":f"Case with id {case_id} does not exists",
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            uploaded_file = request.FILES['file']
            # file_path = self.save_file(uploaded_file)
            file_path = self.upload_file_to_s3(uploaded_file)

            document_paths = case_data.document_paths
            if document_paths is None:
                document_paths = []
            
            document_paths.append(file_path)
            case_data.document_paths = document_paths
            case_data.save()

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
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
                            "user_unauthorized": False,
                            "file_not_attached": False,
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
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

    def upload_file_to_s3(self, uploaded_file):
        """Uploads a file to AWS S3, renaming it if a file with the same name exists."""
        region_name = "eu-north-1"
        s3_client = boto3.client(
            "s3",
            aws_access_key_id = self.decrypt("QUtJQTRUNE9DTTU2TENMUUdTNlA="),
            aws_secret_access_key = self.decrypt("TzRzQmlWK0NvcWdBM2Q1aGhPMXJkeGV0c1YyaWdibjR6YXhrbTRqMA=="),
            region_name = region_name
        )
        
        bucket_name = "ehunt"
        base_name, extension = os.path.splitext(uploaded_file.name)
        file_name = uploaded_file.name
        s3_key = f"uploads/{file_name}"
        counter = 1

        # Check if file exists and rename if necessary
        while True:
            try:
                s3_client.head_object(Bucket=bucket_name, Key=s3_key)
                # If file exists, update the filename
                file_name = f"{base_name}({counter}){extension}"
                s3_key = f"uploads/{file_name}"
                counter += 1
            except s3_client.exceptions.ClientError:
                break  # File does not exist, proceed with upload

        # Upload file
        s3_client.upload_fileobj(uploaded_file, bucket_name, s3_key)

        # Generate file URL
        file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{s3_key}"

        return file_url

    def decrypt(self, b64_text):
        # Decode the Base64 string back to bytes, then to text
        return base64.b64decode(b64_text.encode()).decode()


class SetCaseStatus(viewsets.ViewSet):
    def list(self, request):
        try:
            print('fwraegtrhsyjtgrfwretsrtrhtgraethrsyjtyhtgrfwagetsr')
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

            # user_role = user.role
            # if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin':
            #     return Response(
            #             {
            #                 "success": False,
            #                 "user_not_logged_in": False,
            #                 "user_unauthorized": True,                            
            #                 "data":None,
            #                 "error": None
            #             },
            #             status=status.HTTP_400_BAD_REQUEST
            #         )

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

            case_status = request.GET.get('case_status')
            case_statuses = ['Creation', 'Creation_confirmation', 'Investigation', 'Investigation_confirmation', 'Medical', 'Medical_confirmation', 'Data_entry', 'Data_entry_confirmation', 'Final_report', 'Final_report_confirmation', 'Complete']
            if not case_status or case_status not in case_statuses:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,
                            "data":None,
                            "error": '"case_status" is required'
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
            
            if case_status == 'Investigation_confirmation':
                all_visits_completed = self.check_all_visits(case_id=case_id)
            else:
                all_visits_completed = True

            if all_visits_completed:
                case_data.case_status = case_status
                case_data.save()

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
                        "data":None,
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

    def check_all_visits(self, case_id) -> bool:
        try:
            all_visits = Visit.objects.filter(case_id=case_id, visit_completed=False)
            print(all_visits)
            if all_visits:
                return False
            else:
                return True
        except Exception as e:
            logger.error(e, exc_info=True)
            print(e)
            return False

class AssignMedicalOfficer(viewsets.ViewSet):
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

            user_role = user.role
            if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": True,                            
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

            medical_officer_id = request.data.get('medical_officer_id')
            if not medical_officer_id:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,
                            "data":None,
                            "error": '"medical_officer_id" is required'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_data = Case.objects.get(case_id=case_id)
            if not case_data:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,                            
                            "data":f"Case with id {case_id} does not exists",
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            medical_officer_data = UserDetail.objects.filter(user_id=medical_officer_id).first()
            if not medical_officer_data:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,                        
                        "data":f"medical_officer with id {medical_officer_id} does not exists",
                        "error": None
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            case_data.medical_officer_id = medical_officer_id
            # case_data.case_status = 'Medical_confirmation'
            case_data.save()

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,                        
                        "data":{'case_id':case_id},
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
                            "user_unauthorized": False,                            
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

class AssignDataEntryPersonnel(viewsets.ViewSet):
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

            user_role = user.role
            if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": True,                            
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

            data_entry_personnel_id = request.data.get('data_entry_personnel_id')
            if not data_entry_personnel_id:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,
                            "data":None,
                            "error": '"data_entry_personnel_id" is required'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            case_data = Case.objects.get(case_id=case_id)
            if not case_data:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,                            
                            "data":f"Case with id {case_id} does not exists",
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            data_entry_personnel_data = UserDetail.objects.filter(user_id=data_entry_personnel_id).first()
            if not data_entry_personnel_data:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,                        
                        "data":f"medical_officer with id {data_entry_personnel_id} does not exists",
                        "error": None
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            case_data.data_entry_id = data_entry_personnel_id
            # case_data.case_status = 'Data_entry_confirmation'
            case_data.save()

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,                        
                        "data":{'case_id':case_id},
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
                            "user_unauthorized": False,                            
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

class AddMedicalRemarkCaseViewSet(viewsets.ViewSet):
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

            # user_role = user.role
            # if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin':
            #     return Response(
            #             {
            #                 "success": False,
            #                 "user_not_logged_in": False,
            #                 "user_unauthorized": True,                            
            #                 "data":None,
            #                 "error": None
            #             },
            #             status=status.HTTP_400_BAD_REQUEST
            #         )

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

            medical_remark = request.data.get('medical_remark')
            if not medical_remark:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,
                            "data":None,
                            "error": '"medical_remark" is required'
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
            
            case_details.medical_officer_remarks = medical_remark
            case_data.case_status = 'Medical_confirmation'

            case_details.save()
            case_data.save()

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
                        "data":None,
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

class getDiagnosisData(viewsets.ViewSet):
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

            user_role = user.role
            if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": True,                            
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            query_name = request.data.get('query_name', '')
            if query_name != '':
                case_details = CaseDetails.objects.filter(Q(diagnosis__icontains=query_name))
            else:
                case_details = CaseDetails.objects.all()

            suggestions = []
            for case_info in case_details:
                suggestions.append(case_info.diagnosis)

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
                        "data":{'suggestions': suggestions},
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

class getInsauranceCompanyData(viewsets.ViewSet):
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

            user_role = user.role
            if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": True,                            
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            insaurance_details = InsuranceCompany.objects.all()
            insaurance_data = InsuranceCompanySerializer(insaurance_details, many=True).data

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
                        "data":{'insaurance_data': insaurance_data},
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
                            "user_unauthorized": False,                            
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

class cityData(viewsets.ViewSet):
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

            user_role = user.role
            if user_role != 'coordinator' and user_role != 'hod' and user_role != 'admin':
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unauthorized": True,                            
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            query_name = request.data.get('query_name', '')
            if query_name != '':
                city_details = City.objects.filter(Q(city__icontains=query_name))
            else:
                city_details = City.objects.all()

            city_data = []
            for city_info in city_details:
                city_data.append({'city': city_info.city, 'state':city_info.state})

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
                        "data":{'city_data': city_data},
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
                            "user_unauthorized": False,                            
                            "data":None,
                            "error": str(ex)
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

