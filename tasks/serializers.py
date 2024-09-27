from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task #which model to serialize
        fields = ['id', 'title', 'description', 'due_date', 'completed', 'priority', 'recurrence'] #fields to include in serialization