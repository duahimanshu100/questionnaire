
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from app.utils import pridict_answer


class PredictionApi(APIView):
    """
    Prediction
    """

    def get(self, request):
        query = request.GET.get('query', '')
        if query:
            predicted_lst = pridict_answer(query)
            return Response({'result': predicted_lst})
        else:
            return Response({'error': 'No query provided'})
