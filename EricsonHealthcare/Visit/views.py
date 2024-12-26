from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import VisitSerializer, PharmacyVisitSerializer, LabVisitSerializer, HospitalVisitSerializer
from .models import Visit, LabVisit, HospitalVisit, PharmacyVisit

from Question.models import Question
from Case.models import Case
from Case.serializers import CaseSerializers
from Question.models import Question
from UserRole.models import UserDetail

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
        try:
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

            case_id = request.GET.get('case_id')
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

            case_data = Case.objects.filter(case_id=case_id).first()
            if case_data is None:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "no_visit_for_case": False,
                        "data": None,
                        "error": f"Case with id - {case_id} not found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            investigator_id = request.GET.get('investigator_id')
            if investigator_id:
                visits = Visit.objects.filter(investigator_id=investigator_id, case_id=case_id)
            else:
                visits = Visit.objects.filter(case_id=case_id)

            if not visits and investigator_id:
                return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "no_visit_for_case": True,
                        "data": None,
                        "error": "No visits found for the given case_id and investigator_id."
                    },
                    status=status.HTTP_200_OK
                )

            elif not visits:
                return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "user_unathorized": False,
                        "no_visit_for_case": True,
                        "data": None,
                        "error": "No visits found for the given case_id."
                    },
                    status=status.HTTP_200_OK
                )

            case_visit_details_data = []

            # Collect visit details
            for visit in visits:
                visit_serializer = VisitSerializer(visit)
                visit_data = visit_serializer.data

                visit_type_data = self.get_visit_type_data(visit_data=visit_data)
                if visit_type_data is not False:
                    visit_data['visit_type_data'] = visit_type_data
                
                    final_card_data = visit_data['visit_type_data']
                    final_card_data = {k: v for k, v in final_card_data.items() if k not in ("id", "visit_id", "document_paths", "photo_path", "answers")}
                    
                    visit_questions = []
                    for question_id in final_card_data["questions"]:
                        que = Question.objects.filter(id=question_id).first()
                        if que:
                            visit_questions.append(que.question)

                    final_card_data = {k: v for k, v in final_card_data.items() if k is not "questions"}

                    final_card_data = {
                        key.replace('_', ' ').title(): value
                        for key, value in final_card_data.items()
                    }

                    final_card_data["Investigator"] = UserDetail.objects.filter(user_id=visit_data['investigator_id']).first().name
                    final_card_data["TAT"] = visit_data['tat']

                    visit_data["questions"] = visit_questions

                    visit_data["final_card_data"] = final_card_data


                    case_visit_details_data.append(visit_data)

            return Response(
                {
                    "success": True,
                    "user_not_logged_in": False,
                    "user_unathorized": False,
                    "no_visit_for_case": False,
                    "data": case_visit_details_data,
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

    def get_visit_type_data(self, visit_data):
        try:
            visit_type = str(visit_data.get("type_of_visit", ""))
            if visit_type == 'Hospital':
                visit_type_data_obj = HospitalVisit.objects.filter(visit_id=visit_data.get('visit_id')).first()
                if visit_type_data_obj:
                    visit_type_data = HospitalVisitSerializer(visit_type_data_obj).data
                    return visit_type_data
                return False

            elif visit_type == 'Lab':
                visit_type_data_obj = LabVisit.objects.filter(visit_id=visit_data.get('visit_id')).first()
                if visit_type_data_obj:
                    visit_type_data = LabVisitSerializer(visit_type_data_obj).data
                    return visit_type_data
                return False

            elif visit_type == 'Chemist':
                visit_type_data_obj = PharmacyVisit.objects.filter(visit_id=visit_data.get('visit_id')).first()
                if visit_type_data_obj:
                    visit_type_data = PharmacyVisitSerializer(visit_type_data_obj).data
                    return visit_type_data
                return False

            else:
                return False

        except Exception as e:
            # logger.error(e, exc_info=True)
            print(e)
            return False


class VisitDetailViewSet(viewsets.ViewSet):
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

            visit_id = request.GET.get('visit_id')
            if not visit_id:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": "Please provide Visit ID"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            visit_data_obj = Visit.objects.filter(visit_id=visit_id).first()
            if visit_data_obj is None:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": f"Visit with id - {visit_id} not found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            visit_data = VisitSerializer(visit_data_obj).data
            visit_type_data = self.get_visit_type_data(visit_data=visit_data)
            type_of_visit = str(visit_data['type_of_visit']).lower()

            visit_type_data = {
                        f'{type_of_visit}_{key}': value
                        for key, value in visit_type_data.items()
                    }

            visit_type_data[f'{type_of_visit}_tat'] = visit_data['tat']
    
            for que in visit_type_data[f'{type_of_visit}_questions']:
                visit_type_data[f'question{que}'] = True
            
            visit_data = {**visit_data, **visit_type_data}
            visit_data['edit_visit_id'] = visit_data['visit_id']

            return Response(
                {
                    "success": True,
                    "user_not_logged_in": False,
                    "data": visit_data,
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
                    "data": None,
                    "error": str(ex)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get_visit_type_data(self, visit_data):
        try:
            visit_type = str(visit_data.get("type_of_visit", ""))
            if visit_type == 'Hospital':
                visit_type_data_obj = HospitalVisit.objects.filter(visit_id=visit_data.get('visit_id')).first()
                if visit_type_data_obj:
                    visit_type_data = HospitalVisitSerializer(visit_type_data_obj).data
                    return visit_type_data
                return False

            elif visit_type == 'Lab':
                visit_type_data_obj = LabVisit.objects.filter(visit_id=visit_data.get('visit_id')).first()
                if visit_type_data_obj:
                    visit_type_data = LabVisitSerializer(visit_type_data_obj).data
                    return visit_type_data
                return False

            elif visit_type == 'Chemist':
                visit_type_data_obj = PharmacyVisit.objects.filter(visit_id=visit_data.get('visit_id')).first()
                if visit_type_data_obj:
                    visit_type_data = PharmacyVisitSerializer(visit_type_data_obj).data
                    return visit_type_data
                return False

            else:
                return False

        except Exception as e:
            # logger.error(e, exc_info=True)
            print(e)
            return False


class UpdateVisitViewSet(viewsets.ViewSet):
    def create(self, request):
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

            visit_id = request.data.get('visit_id')
            if not visit_id:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": "Please provide Visit ID"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            visit_data_obj = Visit.objects.get(visit_id=visit_id)
            if visit_data_obj is None:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": f"Visit with id - {visit_id} not found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            request_data = self.rename_keys_based_on_visit(data=request.data)
            visit_type_added = self.handle_visit_type(request_data=request_data)
            if visit_type_added is not False:
                visit_data_obj.investigator_id = request_data['investigator_id']
                visit_data_obj.tat = request_data['tat']
                visit_data_obj.save()

                return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
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
                        "data": None,
                        "error": "Error while updating visit data"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as ex:
            # logger.error(ex, exc_info=True)
            print(ex)
            return Response(
                {
                    "success": False,
                    "user_not_logged_in": False,
                    "data": None,
                    "error": str(ex)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def handle_visit_type(self, request_data):
        try:
            visit_type = str(request_data.get("type_of_visit", ""))
            visit_id = str(request_data.get("visit_id", ""))

            if visit_type == 'Hospital':
                visit_type_data_obj = HospitalVisit.objects.get(visit_id=visit_id)
                visit_type_serializer = HospitalVisitSerializer(instance=visit_type_data_obj, data=request_data, partial=True)

                if visit_type_serializer.is_valid():
                    visit_type_serializer.save()
                    return visit_type_serializer.data

                
                else:
                    # logger.error(visit_type_serializer.errors)
                    print(visit_type_serializer.errors)
                    return False

            elif visit_type == 'Lab':
                visit_type_data_obj = LabVisit.objects.get(visit_id=visit_id)
                visit_type_serializer = LabVisitSerializer(instance=visit_type_data_obj, data=request_data, partial=True)
                if visit_type_serializer.is_valid():
                    visit_type_serializer.save()
                    return visit_type_serializer.data
                
                else:
                    # logger.error(visit_type_serializer.errors)
                    print(visit_type_serializer.errors)
                    return False

            elif visit_type == 'Chemist':
                visit_type_data_obj = PharmacyVisit.objects.get(visit_id=visit_id)
                visit_type_serializer = PharmacyVisitSerializer(instance=visit_type_data_obj, data=request_data, partial=True)

                if visit_type_serializer.is_valid():
                    visit_type_serializer.save()
                    return visit_type_serializer.data
                
                else:
                    # logger.error(visit_type_serializer.errors)
                    print(visit_type_serializer.errors)
                    return False

            else:
                print('hello here')
                return False
        
        except Exception as e:
            # logger.error(e, exc_info=True)
            print(e)
            return False

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


class StartInvestigationVisitViewSet(viewsets.ViewSet):
    def create(self, request):
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

            visit_id = request.data.get('visit_id')
            if not visit_id:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": "Please provide Visit ID"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            visit_data_obj = Visit.objects.get(visit_id=visit_id)
            if visit_data_obj is None:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": f"Visit with id - {visit_id} not found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            visit_data_obj.issue_in_investigation = False
            visit_data_obj.issue_of_investigator = ''
            visit_data_obj.investigation_started = True
            visit_data_obj.save()
        
            return Response(
                {
                    "success": True,
                    "user_not_logged_in": False,
                    "data": 'Investigation started',
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
                    "data": None,
                    "error": str(ex)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RaiseVisitIssueViewSet(viewsets.ViewSet):
    def create(self, request):
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

            issue_text = request.data.get('issue_text')
            if not issue_text:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": "Please provide issue_text"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )


            visit_id = request.data.get('visit_id')
            if not visit_id:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": "Please provide Visit ID"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            visit_data_obj = Visit.objects.get(visit_id=visit_id)
            if visit_data_obj is None:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": f"Visit with id - {visit_id} not found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            visit_data_obj.issue_in_investigation = True
            visit_data_obj.issue_of_investigator = issue_text
            visit_data_obj.save()
        
            return Response(
                {
                    "success": True,
                    "user_not_logged_in": False,
                    "data": 'Investigation started',
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
                    "data": None,
                    "error": str(ex)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

