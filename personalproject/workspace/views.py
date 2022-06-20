from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

class WorkspaceListCreateView(generics.ListCreateAPIView):
    queryset = models.Workspace.objects.all()
    # serializer_class = serializers.WorkspaceWriteSerializer
    permission_classes = []

    def get_serializer_class(self):
        # return super().get_serializer_class()
        if self.request.method == 'GET':
            return serializers.WorkspaceOnlyReadSerializer 
        return serializers.WorkspaceOnlyWriteSerializer
    
class WorkspaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Workspace.objects.all()
    # serializer_class = serializers.WorkspaceWriteSerializer
    permission_classes = []
    # lookup_field = 'workspace_id'
    lookup_url_kwarg = 'workspace_id'
    def get_serializer_class(self):        
        if self.request.method == 'GET':
            self.serializer_class =  serializers.WorkspaceOnlyReadSerializer 
        else:
            self.serializer_class = serializers.WorkspaceOnlyWriteSerializer
        return super().get_serializer_class()
