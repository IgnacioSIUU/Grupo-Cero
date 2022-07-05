from dataclasses import fields
from pyexpat import model
from .models import Arte
from rest_framework import serializers

class ArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arte
        fields = '__all__'