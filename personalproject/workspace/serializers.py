from rest_framework import serializers
from . import models

class WorkspaceOnlyWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Workspace
        fields = ['title', 'description', 'url']
        extra_kwargs = {
            'title': {'write_only': True},
            'description': {'write_only': True},
            'url': {'write_only': True},
            # 'auth_id': {'write_only': True},
            # 'id': {'id': True}
        }
        
class WorkspaceOnlyReadSerializer(serializers.ModelSerializer):
    auth_id = serializers.StringRelatedField()
    class Meta:
        model = models.Workspace
        fields = '__all__'
        read_only_fields = ['title', 'description', 'url', 'auth_id', 'id']