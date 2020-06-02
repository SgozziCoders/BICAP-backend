from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from BICAPweb.models import *
from .serializers import *

    ####################################################################
    #######################      ADMIN ONLY      #######################
    ####################################################################
class IndagineListCreateAPIView(generics.ListCreateAPIView):
    queryset = Indagine.objects.all().order_by("id")
    serializer_class = IndagineSerializer
    permission_classes = [permissions.IsAdminUser]
    #pagination_class = SmallSetPagination

class DistribuzioneCreateAPIView(generics.ListCreateAPIView):
    queryset = Distribuzione.objects.all()
    serializer_class = DistribuzioneSerializer
    permission_classes = [permissions.IsAdminUser]
    #pagination_class = SmallSetPagination


    ####################################################################
    #######################        PUBLIC        #######################
    ####################################################################

class IndagineDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Indagine.objects.all()
    serializer_class = IndagineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    ####################################################################
    #######################      PUBLIC-APP      #######################
    ####################################################################
class IndagineBodyAPIView(generics.RetrieveAPIView):
    queryset = Indagine.objects.all()
    serializer_class = IndagineBodySerializer


class IndagineHeadListAPIView(APIView):
    """ 
    API che accetta come parametro la mail e restituisce una lista di indagineHead 
    """

    def getIndaginiFromDistribuzioni(self, distribuzioni):
        """ 
        Metodo che data una lista di distrubizioni crea una lista di indagini 
        """
        indagineList = []
        for distribuzione in distribuzioni:
            indagineList.append(distribuzione.indagine)
        return indagineList

    def get(self, request):
        email = self.request.query_params.get('email')   
        utente = get_object_or_404(Utente, email=email)
        distribuzioni = Distribuzione.objects.all().filter(utente=utente, terminata=False)
        serializer = IndagineHeadSerializer(self.getIndaginiFromDistribuzioni(distribuzioni), many=True)
        response = { 'indagine' : serializer.data }
        return Response(response)


class DistribuzioneMinimalDetailAPIView(APIView):
    """ 
    API che accetta come parametro la mail e id dell'indagine e restituisce una distribuzione 
    """

    def get_object(self):
        email = self.request.query_params.get('email')   
        idIndagine = self.request.query_params.get('idIndagine')  
        utente = get_object_or_404(Utente, email=email)
        distribuzione = get_object_or_404(Distribuzione, utente=utente, indagine=idIndagine)
        return distribuzione

    def get(self, request):
        distribuzione = self.get_object()
        serializer = DistribuzioneMinimalSerializer(distribuzione)
        return Response(serializer.data)

    def put(self, request):
        distribuzione = self.get_object()
        serializer = DistribuzioneMinimalSerializer(distribuzione, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)