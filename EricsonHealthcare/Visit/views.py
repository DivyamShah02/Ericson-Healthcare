from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import VisitSerializer, PharmacyVisitSerializer, LabVisitSerializer, HospitalVisitSerializer
from . models import Visit, LabVisit, HospitalVisit, PharmacyVisit

from Question.models import Question
from Case.models import Case

from Case.serializers import CaseSerializers

class VisitCreationViewSet(viewsets.ViewSet):
    
    def create(self, request):
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_questions_from_id(self, questions_id_lst):
        filtered_questions = Question.objects.filter(id__in=questions_id_lst)
        questions = list(filtered_questions.values_list('question', flat=True))
        return questions

    @action(detail=False, methods=['post'], url_path='get-visit-by-investigator-case')
    def get_visit_details(self, request):
        investigator_id = request.data.get('investigator_id')
        case_id = request.data.get('case_id')

        # Ensure case_id is provided
        if not case_id:
            return Response({"error": "case_id is required."}, status=400)

        try:
            # If both investigator_id and case_id are provided, filter by both
            if investigator_id:
                visits = Visit.objects.filter(investigator_id=investigator_id, case_id=case_id)
            else:
                # If only case_id is provided, retrieve all visits for the case_id
                print("case id is", case_id)
                visits = Visit.objects.filter(case_id=case_id)
                print("visits", visits)

            if not visits and investigator_id:
                return Response({"error": "No visits found for the given case_id and investigating officer id."}, 
                                status=status.HTTP_400_BAD_REQUEST)
            elif not visits:
                return Response({"error": "No visits found for the given case_id."}, 
                                status=status.HTTP_400_BAD_REQUEST)


            visit_serializer = VisitSerializer(visits, many=True)
            response_data = []

            # Collect visit details
            for visit in visits:
                visit_serializer = VisitSerializer(visit)
                visit_data = visit_serializer.data

                visit_detail = {"visit": visit_data}

                # Check if the visit has an associated HospitalVisit, LabVisit, or PharmacyVisit
                if HospitalVisit.objects.filter(visit_id=visit.visit_id).exists():
                    hospital_visit = HospitalVisit.objects.get(visit_id=visit.visit_id)
                    hospital_visit_serializer = HospitalVisitSerializer(hospital_visit)
                    visit_detail["visit_type"] = hospital_visit_serializer.data
                    visit_detail["visit_type"]["visit_type"] = "Hospital"

                    questions_ids_lst = list(hospital_visit_serializer.data["questions"].values())
                    if questions_ids_lst:
                        questions = self.get_questions_from_id(questions_ids_lst)
                        visit_detail["visit_type"]["questions"] = questions

                elif LabVisit.objects.filter(visit_id=visit.visit_id).exists():
                    lab_visit = LabVisit.objects.get(visit_id=visit.visit_id)
                    lab_visit_serializer = LabVisitSerializer(lab_visit)
                    visit_detail["visit_type"] = lab_visit_serializer.data
                    visit_detail["visit_type"]["visit_type"] = "Lab"

                    questions_ids_lst = list(lab_visit_serializer.data["questions"].values())
                    if questions_ids_lst:
                        questions = self.get_questions_from_id(questions_ids_lst)
                        visit_detail["visit_type"]["questions"] = questions

                elif PharmacyVisit.objects.filter(visit_id=visit.visit_id).exists():
                    pharmacy_visit = PharmacyVisit.objects.get(visit_id=visit.visit_id)
                    pharmacy_visit_serializer = PharmacyVisitSerializer(pharmacy_visit)
                    visit_detail["visit_type"] = pharmacy_visit_serializer.data
                    visit_detail["visit_type"]["visit_type"] = "Pharmacy"

                    questions_ids_lst = list(pharmacy_visit_serializer.data["questions"].values())
                    if questions_ids_lst:
                        questions = self.get_questions_from_id(questions_ids_lst)
                        visit_detail["visit_type"]["questions"] = questions

                else:
                    visit_detail["details"] = "No associated visit details found."

                response_data.append(visit_detail)

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



