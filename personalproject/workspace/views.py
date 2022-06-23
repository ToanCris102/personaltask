from django.shortcuts import render
from rest_framework import generics, permissions, response, status
from . import models
from . import serializers
from account.permissions import IsOwner
from .permissions import IsOwnerWorkspace


# @access Private: Users with their Token
# @method GET, POST
# @desc For list workspace, and create workspace
class WorkspaceListCreateView(generics.ListCreateAPIView):    
    permission_classes = [IsOwner, permissions.IsAuthenticated] 
    # can remove IsOwner because line 16
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.WorkspaceOnlyReadSerializer 
        return serializers.WorkspaceOnlyWriteSerializer
    
    def get_queryset(self):        
        self.queryset = models.Workspace.objects.filter(auth_id=self.request.user)
        return super().get_queryset()
    
    def perform_create(self, serializer):        
        serializer.save(auth_id=self.request.user)

# @access Private: Users with their Token
# @method GET,PUT,PATCH,DELETE
# @desc For review detail OR destroy, update Workspace data
class WorkspaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerWorkspace, IsOwner, permissions.IsAuthenticated]
    # You can remove IsOwnerWorkspace, IsOwner because line 34
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