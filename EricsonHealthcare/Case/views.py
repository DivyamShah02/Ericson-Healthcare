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

        return Response(serializer.data)


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