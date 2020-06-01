from rest_framework import serializers
from BICAPweb.models import *

class QuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionario
        fields = "__all__"

class IndagineBodySerializer(serializers.ModelSerializer):
    questionari = QuestionarioSerializer(many=True, read_only=True)

    class Meta:
        model = Indagine
        fields = ('titoloIndagine','erogatore', 'questionari')

