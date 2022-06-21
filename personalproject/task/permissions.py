from rest_framework import permissions
from . import models
from django.forms import ValidationError
class IsOwnerTask(permissions.BasePermission):
 
    def has_permission(self, request, view):
        try: 
            owner = models.Task.objects.get(workspace_id=view.kwargs['workspace_id'])
        except:
            return False
        return request.user == owner.auth_id
        # return False
            
        