from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from BICAPweb.models import *
from .serializers import *

class IndagineCreateAPIView(APIView):
    """
    Ritorna l'elenco delle indagini
    """

    def get(self, request):
        indagini = Indagine.objects.filter()
        serializer = IndagineBodySerializer(indagini, many=True)
        return Response(serializer.data)

