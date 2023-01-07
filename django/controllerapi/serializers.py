from dataclasses import fields
from rest_framework import serializers
from .models import *
  
class TaskSerializer(serializers.ModelSerializer):
    id = serializers.JSONField()
    class Meta:
        model = Task
        fields = ('__all__')
        # OR:
        # fields = ['id', 'name','type', 'active', 'frequency']