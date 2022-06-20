from functools import partial
from urllib import request
from django.shortcuts import render
from rest_framework import generics, permissions, response, status
from . import models
from . import serializers
from account.permissions import IsOwnerOrReadOnly

class WorkspaceListCreateView(generics.ListCreateAPIView):
    # queryset = models.Workspace.objects.all()
    # serializer_class = serializers.WorkspaceWriteSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        # return super().get_serializer_class()
        if self.request.method == 'GET':
            return serializers.WorkspaceOnlyReadSerializer 
        return serializers.WorkspaceOnlyWriteSerializer
    
    def get_queryset(self):        
        self.queryset = models.Workspace.objects.filter(auth_id=self.request.user)
        return super().get_queryset()
    
    def perform_create(self, serializer):        
        serializer.save(auth_id=self.request.user)
    
class WorkspaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = 'workspace_id'
    def get_serializer_class(self):        
        if self.request.method == 'GET':
            self.serializer_class =  serializers.WorkspaceOnlyReadSerializer 
        else:
            self.serializer_class = serializers.WorkspaceOnlyWriteSerializer
        return super().get_serializer_class()
    
    def get_queryset(self):        
        self.queryset = models.Workspace.objects.filter(auth_id=self.request.user)
        return super().get_queryset()