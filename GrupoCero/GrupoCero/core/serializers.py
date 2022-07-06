from dataclasses import fields
from pyexpat import model
from core.models import Arte
from rest_framework import serializers

class ArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arte
        fields = ['idprod','nombre','precio','tecnica','autor','categoria']