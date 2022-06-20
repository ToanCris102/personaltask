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
            return serializers.WorkspaceReadSerializer 
        return serializers.WorkspaceReadSerializer
    
class WorkspaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Workspace.objects.all()
    # serializer_class = serializers.WorkspaceWriteSerializer
    permission_classes = []
    # lookup_field = 'workspace_id'
    lookup_url_kwarg = 'workspace_id'
    def get_serializer_class(self):
        # return super().get_serializer_class()
        if self.request.method == 'GET':
            return serializers.WorkspaceReadSerializer 
        return serializers.WorkspaceReadSerializer
