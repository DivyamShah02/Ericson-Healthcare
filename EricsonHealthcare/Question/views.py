from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Question
from .serializers import QuestionSerializers
from Case.models import Case, CaseDetails
from Visit.models import Visit, LabVisit, HospitalVisit, PharmacyVisit
from Visit.serializers import VisitSerializer, PharmacyVisitSerializer, LabVisitSerializer, HospitalVisitSerializer


# Create your views here.
class QuestionViewSet(viewsets.ViewSet):
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
            
            question_text = request.data.get('question')
            type_of_visit = request.data.get('type_of_visit')
            if not question_text:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
                        "data": None,
                        "error": "Please provide question"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            question_obj = Question.objects.create(question=question_text, visit_type=type_of_visit)
            question_obj.save()

            return Response(
                        {
                            "success": True,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,
                            "data": "Question added successfully",
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
                        "data": None,
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
                            "user_unauthorized": False,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            type_of_visit = request.GET.get('type_of_visit')
            if type_of_visit:
                print(type_of_visit)
                all_question_obj = Question.objects.filter(visit_type=type_of_visit)
            else:
                all_question_obj = Question.objects.all()
            all_question = QuestionSerializers(all_question_obj, many=True).data

            return Response(
                        {
                            "success": True,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,
                            "data":all_question,
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
                        "data": None,
                        "error": str(ex)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

class VisitQuestionViewSet(viewsets.ViewSet):
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

            visit_data = Visit.objects.filter(visit_id=visit_id).first()
            if not visit_data:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": f"Visit with id - {visit_id} not found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            visit_type_data = self.get_visit_type_data(visit_data=visit_data)
            if visit_type_data is False:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "user_unauthorized": False,
                        "data": None,
                        "error": "Error occured while getting visit type details"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            answers_dict = visit_type_data["answers"]
            if answers_dict is None or answers_dict == '':
                answers_dict = {}
            
            questions_id_lst = visit_type_data["questions"]
            questions = []
            for que_id in questions_id_lst:
                question_data = Question.objects.filter(id=que_id).first()
                question_temp_dict = {
                    'question': question_data.question,
                    'answer':False
                }
                if que_id in answers_dict.keys():
                    if str(answers_dict[que_id]) != '':
                        question_temp_dict['answer'] = answers_dict[que_id]

                questions.append(question_temp_dict)

            return Response(
                        {
                            "success": True,
                            "user_not_logged_in": False,
                            "user_unauthorized": False,
                            "data":questions,
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
                        "data": None,
                        "error": str(ex)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

    def create(self, request):
        try:
            user = request.user
            # if not user.is_authenticated:
            #     return Response(
            #             {
            #                 "success": False,
            #                 "user_not_logged_in": True,
            #                 "data":None,
            #                 "error": None
            #             },
            #             status=status.HTTP_400_BAD_REQUEST
            #         )

            visit_id = request.data.get('visit_id')
            answers = request.data.get('answers')

            # Validate that 'visit_id' and 'answers' are present
            if not visit_id:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": "visit_id is required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not answers:
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": "answer is required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                # Check if a visit with the given 'visit_id' exists
                visit = Visit.objects.get(visit_id=visit_id)
            except Visit.DoesNotExist:
                # If the visit doesn't exist, return a 404 error
                return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": "Visit ID does not exists"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Get visit type from Visit
            visit_type = visit.type_of_visit

            if visit_type == 'Hospital':
                visit_type_obj = HospitalVisit.objects.get(visit_id=visit_id)
            if visit_type == 'Lab':
                visit_type_obj = LabVisit.objects.get(visit_id=visit_id)
            elif visit_type == 'Chemist':
                visit_type_obj = PharmacyVisit.objects.get(visit_id=visit_id)

            # Get current visit questions list
            current_visit_questions = visit_type_obj.questions
            result = {
                current_visit_questions[int(k)]: v
                for k, v in answers.items()
                if int(k) < len(current_visit_questions)
            }

            # Update the answers field
            if visit_type_obj.answers is None:
                visit_answers = {}
            else:
                visit_answers = visit_type_obj.answers
            visit_answers.update(result)  # Update the existing dictionary with new key-value pairs
            visit_type_obj.answers = visit_answers
            visit_type_obj.save()
            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "data": "Successfully Updated the answer table",
                        "error": None
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                    {
                        "success": False,
                        "user_not_logged_in": False,
                        "data": None,
                        "error": f"Error Occurred {e}"
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    def get_visit_type_data(self, visit_data):
        try:
            visit_type = str(visit_data.type_of_visit)
            if visit_type == 'Hospital':
                visit_type_data_obj = HospitalVisit.objects.filter(visit_id=visit_data.visit_id).first()
                if visit_type_data_obj:
                    visit_type_data = HospitalVisitSerializer(visit_type_data_obj).data
                    return visit_type_data
                return False

            elif visit_type == 'Lab':
                visit_type_data_obj = LabVisit.objects.filter(visit_id=visit_data.visit_id).first()
                if visit_type_data_obj:
                    visit_type_data = LabVisitSerializer(visit_type_data_obj).data
                    return visit_type_data
                return False

            elif visit_type == 'Chemist':
                visit_type_data_obj = PharmacyVisit.objects.filter(visit_id=visit_data.visit_id).first()
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

