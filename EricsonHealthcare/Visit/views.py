from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import VisitSerializer, PharmacyVisitSerializer, LabVisitSerializer, HospitalVisitSerializer
from . models import Visit, LabVisit, HospitalVisit, PharmacyVisit

class VisitCreationViewSet(viewsets.ViewSet):
    
    def create(self, request):
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='get-visit-by-investigator-case')
    def get_visit_details(self, request):
        investigator_id = request.data.get('investigator_id')
        case_id = request.data.get('case_id')

        if not investigator_id or not case_id:
            return Response({"error": "investigator_id and case_id are required."}, status=400)
        
        try:
            visit = Visit.objects.filter(investigator_id=investigator_id, case_id=case_id).first()
            
            if not visit:
                return Response({"error": "No visits found for the given investigator_id and case_id."}, status=404)
            
            visit_serializer = VisitSerializer(visit)
            visit_data = visit_serializer.data

            response_data = {"visit": visit_data}

            if HospitalVisit.objects.filter(visit_id=visit.visit_id).exists():
                hospital_visit = HospitalVisit.objects.get(visit_id=visit.visit_id)
                hospital_visit_serializer = HospitalVisitSerializer(hospital_visit)
                response_data["hospital_visit"] = hospital_visit_serializer.data
            elif LabVisit.objects.filter(visit_id=visit.visit_id).exists():
                lab_visit = LabVisit.objects.get(visit_id=visit.visit_id)
                lab_visit_serializer = LabVisitSerializer(lab_visit)
                response_data["lab_visit"] = lab_visit_serializer.data
            elif PharmacyVisit.objects.filter(visit_id=visit.visit_id).exists():
                pharmacy_visit = PharmacyVisit.objects.get(visit_id=visit.visit_id)
                pharmacy_visit_serializer = PharmacyVisitSerializer(pharmacy_visit)
                response_data["pharmacy_visit"] = pharmacy_visit_serializer.data
            else:
                response_data["details"] = "No associated visit details found."

            return Response(response_data, status=status.HTTP_200_OK)      

        except Exception as ex:
            return Response({"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

