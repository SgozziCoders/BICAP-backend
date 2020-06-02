from django.urls import path, include
from BICAPweb.api.views import (IndagineListCreateAPIView, 
                                DistribuzioneCreateAPIView, 
                                IndagineDetailAPIView, 
                                IndagineBodyAPIView, 
                                IndagineHeadListAPIView,
                                DistribuzioneMinimalDetailAPIView)

urlpatterns = [
    ####################################################################
    #######################      ADMIN ONLY      #######################
    ####################################################################
    path('indagini/', 
         IndagineListCreateAPIView.as_view(), 
         name="indagini-list"),

    path('distribuzioni/', 
         DistribuzioneCreateAPIView.as_view(), 
         name="distribuzione-list"),


    ####################################################################
    #######################        PUBLIC        #######################
    ####################################################################
    path("indagine/by-id/<int:pk>", 
         IndagineDetailAPIView.as_view(), 
         name="indagine-detail"),

    
    ####################################################################
    #######################      PUBLIC-APP      #######################
    ####################################################################
    path("indaginebody/by-id/<int:pk>", 
         IndagineBodyAPIView.as_view(), 
         name="indagineBody-detail"),

    path("indagineHeadList/", 
         IndagineHeadListAPIView.as_view(), 
         name="indagineHeadList-detail"),

    path('distribuzione/', 
         DistribuzioneMinimalDetailAPIView.as_view(), 
         name="distribuzione-list"),
    
    #Distribuzione put par1: id-utente  par2: idIndagine
    #path('distribuzione/.... DistribuzioneCreateAPIView.as_view(), name="distribuzione-list")
]