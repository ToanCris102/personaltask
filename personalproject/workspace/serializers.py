from rest_framework import serializers
from . import models

class WorkspaceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Workspace
        fields = ['title', 'description', 'url', 'auth_id']
        extra_kwargs = {
            'title': {'write_only': True},
            'description': {'write_only': True},
            'url': {'write_only': True},
            'auth_id': {'write_only': True},
            # 'id': {'id': True}
        }
        
class WorkspaceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Workspace
        fields = '__all__'
        read_only_fields = ["breed_name","owner_email"]