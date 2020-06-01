from django.urls import path, include
from BICAPweb.api.views import IndagineCreateAPIView

urlpatterns = [
    path('indagini/', IndagineCreateAPIView.as_view(), name="indagini-list")
]