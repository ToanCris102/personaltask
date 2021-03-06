from ast import And
from django.forms import ValidationError
from django.shortcuts import render
from rest_framework import generics, filters, permissions
from rest_framework.response import Response
from . import serializers
from . import models
from workspace.models import Workspace
from django_filters.rest_framework import DjangoFilterBackend
from account.permissions import IsOwner
from workspace.permissions import IsOwnerWorkspace

# @access Private: Users with their Token
# @method POST and GET
# @desc For create Task and show List Task
class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerWorkspace]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['status_id__status_name', 'name', 'priority_id__priority_name']
    filterset_fields = ['status_id']
    def get_queryset(self):        
        self.queryset = models.Task.objects.filter(workspace_id=self.kwargs['workspace_id']).select_related()      
        return super().get_queryset()

    def get_serializer_class(self):        
        if self.request.method == 'GET':
            self.serializer_class =  serializers.TaskOnlyReadSerializer 
        else:
            self.serializer_class = serializers.TaskOnlyWriteSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        try:
            workspace_temp = Workspace.objects.get(id=self.kwargs['workspace_id'])
            # if workspace_temp.auth_id != self.request.user:
            #     ValidationError('The workspace is not yours')
        except:
            ValidationError('The workspace dont exist')
        return serializer.save(workspace_id=workspace_temp)

# @access Private: Users with their Token
# @method GET,PUT,PATCH,DELETE
# @desc For review detail task OR destroy, update Task data
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerWorkspace, permissions.IsAuthenticated]
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
    
    