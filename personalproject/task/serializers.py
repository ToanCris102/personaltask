from dataclasses import field
from rest_framework import serializers
from . import models

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Priority
        fields = '__all__'
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'
        
        
class TaskOnlyWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        # fields = ['name', 'workspace_id', 'priority_id', 'status_id', 'description', 'due_date ']
        exclude = ['id', 'created_date', 'created_time', 'status_id', 'workspace_id']
        extra_kwargs = {
            'name': {'write_only': True},
            'description': {'write_only': True},
            'workspace_id': {'write_only': True},
            'priority_id': {'write_only': True},
            'due_date': {'write_only': True},
        }    

class TaskOnlyReadSerializer(serializers.ModelSerializer):
    workspace_id = serializers.StringRelatedField()
    priority_id = serializers.StringRelatedField()
    status_id = serializers.StringRelatedField()
    class Meta:
        model = models.Task
        # depth = 1
        # fields = ['name', 'workspace_id', 'priority_id', 'status_id', 'description', 'due_date']
        fields = '__all__'
        
        read_only_fields = ['id', 'name', 'workspace_id', 'priority_id', 'status_id', 'description', 'due_date']