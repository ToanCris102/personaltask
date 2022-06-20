from ast import And
from django.shortcuts import render
from rest_framework import generics, filters
from . import serializers
from . import models
from workspace.models import Workspace
from django_filters.rest_framework import DjangoFilterBackend
from account.permissions import IsOwnerOrReadOnly

class TaskListCreateView(generics.ListCreateAPIView):
    # serializer_class = serializers.TaskOnlyReadSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['status_id__status_name', 'name', 'priority_id__priority_name']
    filterset_fields = ['status_id']
    def get_queryset(self):        
        self.queryset = models.Task.objects.filter(workspace_id=self.kwargs['workspace_id'])
        return super().get_queryset()

    def get_serializer_class(self):        
        if self.request.method == 'GET':
            self.serializer_class =  serializers.TaskOnlyReadSerializer 
        else:
            self.serializer_class = serializers.TaskOnlyWriteSerializer
        return super().get_serializer_class()
    
    
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = 'task_id'
    def get_serializer_class(self):        
        if self.request.method == 'GET':
            self.serializer_class =  serializers.TaskOnlyReadSerializer 
        else:
            self.serializer_class = serializers.TaskOnlyWriteSerializer
        return super().get_serializer_class()
    
    def get_queryset(self):        
        self.queryset = models.Task.objects.filter(workspace_id=self.kwargs['workspace_id'])
        return super().get_queryset()
    
    