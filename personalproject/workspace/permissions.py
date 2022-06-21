from rest_framework import permissions
from . import models
from django.forms import ValidationError
class IsOwnerWorkspace(permissions.BasePermission):
 
    def has_permission(self, request, view):
        try: 
            owner = models.Workspace.objects.get(id=view.kwargs['workspace_id'])
        except:
            return False
        return request.user == owner.auth_id
        # return False
            
        