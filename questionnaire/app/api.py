
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from app.utils import pridict_answer, add_new_questionnaire


class PredictionApi(APIView):
    """
    Prediction
    """

    def get(self, request):
        query = request.GET.get('query', '')
        if query:
            predicted_lst = pridict_answer(query)
            return Response({'answers': predicted_lst})
        else:
            return Response({'error': 'No query provided'})

    def post(self, request):
        question = request.POST.get('question', '')
        answer = request.POST.get('answer', '')
        if question and answer:
            add_new_questionnaire(question, answer)
            return Response({'result': True})
        else:
            return Response({'error': 'No data provided'})
