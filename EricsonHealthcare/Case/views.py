from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import CaseSerializers, CaseDetailsSerializer
from .models import Case, CaseDetails
from rest_framework.decorators import action

# Create your views here.

class CaseViewSet(viewsets.ViewSet):
    
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
        

class CaseDetailsViewSet(viewsets.ViewSet):
    
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