from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer



#Creating views

class TaskListCreateView(generics.ListCreateAPIView): #lists all tasks and also creates new tasks
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): #Handles Get,Put and Delete requests
    queryset = Task.objects.all()
    serializer_class = TaskSerializer