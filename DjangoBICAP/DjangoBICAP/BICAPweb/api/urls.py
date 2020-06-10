from django.urls import path, include
from BICAPweb.api.views import (IndagineListCreateAPIView, 
                                DistribuzioneListCreateAPIView, 
                                IndagineDetailAPIView, 
                                IndagineBodyAPIView, 
                                IndagineHeadListAPIView,
                                DistribuzioneMinimalDetailAPIView)

urlpatterns = [
########################################################################
#########################      ADMIN ONLY      #########################
########################################################################
    path('indagini/', 
         IndagineListCreateAPIView.as_view(), 
         name="indagini-list"),

    path('distribuzioni/', 
         DistribuzioneListCreateAPIView.as_view(), 
         name="distribuzione-list"),


########################################################################
#########################        PUBLIC        #########################
########################################################################
    path("indagine/by-id/<int:pk>", 
         IndagineDetailAPIView.as_view(), 
         name="indagine-detail"),

    
########################################################################
#########################      PUBLIC-APP      #########################
########################################################################
    path("indaginebody/by-id/<int:pk>", 
         IndagineBodyAPIView.as_view(), 
         name="indagineBody-detail"),

    #/api/indagineHeadList/?email=<email>
    path("indagineHeadList/", 
         IndagineHeadListAPIView.as_view(), 
         name="indagineHeadList-detail"),

    #/api/distribuzione/?email=<email>&idIndagine=<idIndagine>
    path('distribuzione/', 
         DistribuzioneMinimalDetailAPIView.as_view(), 
         name="distribuzione-list"),
    
    #Distribuzione put par1: id-utente  par2: idIndagine
    #path('distribuzione/.... DistribuzioneCreateAPIView.as_view(), name="distribuzione-list")
]