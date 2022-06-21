from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.id), filename])

class Workspace(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    auth_id = models.ForeignKey(User, related_name='workspaces', on_delete=models.CASCADE)
    url = models.ImageField(upload_to=nameFile, blank=True, null=True)
    # url = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self) -> str:
        return self.title
    
