from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import VisitSerializer, PharmacyVisitSerializer, LabVisitSerializer, HospitalVisitSerializer
from .models import Visit, LabVisit, HospitalVisit, PharmacyVisit

from Question.models import Question
from Case.models import Case
from Case.serializers import CaseSerializers

import random

logger = None

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


class VisitViewSet(viewsets.ViewSet):
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
                        "data": None,
                        "error": "Please provide Case ID"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            case_obj = Case.objects.filter(case_id=case_id).first()
            if case_obj is None:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "data": None,
                            "error": f"Case with id - {case_id} not found"
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            new_visit_id = True
            while new_visit_id:
                visit_id = random.randint(1111111111,9999999999)
                if len(Visit.objects.filter(visit_id=visit_id)) == 0:
                    new_visit_id = False

            request_data = self.rename_keys_based_on_visit(data=request.data)
            request_data['visit_id'] = visit_id

            new_visit = Visit(visit_id=visit_id,
                                case_id=case_id,
                                coordinator_id=case_obj.coordinator_id,
                                investigator_id=request_data['investigator_id'],
                                type_of_visit=request_data['type_of_visit'],
                                tat=request_data['tat'],
                                visit_status='Investigation'
                            )

            visit_type_added = self.handle_visit_type(request_data=request_data)
            if visit_type_added:
                new_visit.save()

                return Response(
                        {
                            "success": True,
                            "user_not_logged_in": False,
                            "user_unathorized": False,
                            "data": request_data,
                            "error": None
                        },
                        status=status.HTTP_200_OK
                    )

            else:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "data": None,
                        "error": 'Error occured unable to save the visit'
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        except Exception as ex:
            # logger.error(ex, exc_info=True)
            print(ex)
            return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "data": None,
                        "error": str(ex)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    def rename_keys_based_on_visit(self, data):
        visit_type = str(data.get("type_of_visit", "")).lower()
        if not visit_type:
            return data
        updated_data = {}
        for key, value in data.items():
            if key.startswith(visit_type + "_"):
                new_key = key[len(visit_type) + 1:]
                updated_data[new_key] = value
            else:
                updated_data[key] = value
        return updated_data

    def handle_visit_type(self, request_data):
        try:
            visit_type = str(request_data.get("type_of_visit", ""))

            if visit_type == 'Hospital':
                visit_type_data_obj = HospitalVisitSerializer(data=request_data)
                if visit_type_data_obj.is_valid():
                    visit_type_data_obj.save()
                    return True
                else:
                    # logger.error(visit_type_data_obj.errors)
                    print(visit_type_data_obj.errors)
                    return False

            elif visit_type == 'Lab':
                visit_type_data_obj = LabVisitSerializer(data=request_data)
                if visit_type_data_obj.is_valid():
                    visit_type_data_obj.save()
                    return True
                else:
                    # logger.error(visit_type_data_obj.errors)
                    print(visit_type_data_obj.errors)
                    return False

            elif visit_type == 'Chemist':
                visit_type_data_obj = PharmacyVisitSerializer(data=request_data)
                if visit_type_data_obj.is_valid():
                    visit_type_data_obj.save()
                    return True
                else:
                    # logger.error(visit_type_data_obj.errors)
                    print(visit_type_data_obj.errors)
                    return False

            else:
                print('hello here')
                return False
        
        except Exception as e:
            # logger.error(e, exc_info=True)
            print(e)
            return False

    def list(self, request):
        """
        Custom POST method to get visit details by investigator and case ID.
        """
        user = request.user

        if not user.is_authenticated:
            return Response(
                    {
                        "success": False,
                        "user_not_logged_in": True,
                        "user_unathorized": False,
                        "no_visit_for_case": False,
                        "data":None,
                        "error": None
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        case_id = request.data.get('case_id')
        
        # Ensure case_id is provided
        if not case_id:
            return Response(
                {
                    "success": False,
                    "user_not_logged_in": False,
                    "user_unathorized": False,
                    "no_visit_for_case": False,
                    "data": None,
                    "error": "Please provide Case ID"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Ensure case_id is a valid integer
        try:
            case_id = int(case_id)
        except ValueError:
            return Response(
                {
                    "success": False,
                    "user_not_logged_in": False,
                    "user_unathorized": False,
                    "no_visit_for_case": False,
                    "data": None,
                    "error": "Case ID must be a valid integer."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        investigator_id = request.data.get('investigator_id')

        try:
            # If both investigator_id and case_id are provided, filter by both
            if investigator_id:
                visits = Visit.objects.filter(investigator_id=investigator_id, case_id=case_id)
            else:
                visits = Visit.objects.filter(case_id=case_id)

            if not visits and investigator_id:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "no_visit_for_case": True,
                        "data": None,
                        "error": "No visits found for the given case_id and investigator_id."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            elif not visits:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "no_visit_for_case": True,
                        "data": None,
                        "error": "No visits found for the given case_id."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            case_details_data = []

            # Collect visit details
            for visit in visits:
                visit_serializer = VisitSerializer(visit)
                visit_data = visit_serializer.data
                visit_detail = {"visit": visit_data}

                # Check for associated HospitalVisit, LabVisit, or PharmacyVisit
                visit_detail = self.add_visit_type_details(visit, visit_detail)

                case_details_data.append(visit_detail)

            return Response(
                {
                    "success": True,
                    "user_not_logged_in": False,
                    "user_unathorized": False,
                    "no_visit_for_case": False,
                    "data": case_details_data,
                    "error": None
                },
                status=status.HTTP_200_OK
            )

        except Exception as ex:
            logger.error(ex, exc_info=True)
            return Response(
                {
                    "success": False,
                    "user_not_logged_in": False,
                    "user_unathorized": False,
                    "no_visit_for_case": False,
                    "data": None,
                    "error": str(ex)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get_questions_from_id(self, questions_id_lst):
        """
        Helper method to fetch questions from their IDs.
        """
        filtered_questions = Question.objects.filter(id__in=questions_id_lst)
        return list(filtered_questions.values_list('question', flat=True))

    def add_visit_type_details(self, visit, visit_detail):
        """
        Helper method to add details related to HospitalVisit, 
        LabVisit, or PharmacyVisit.
        """
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

        return visit_detail
