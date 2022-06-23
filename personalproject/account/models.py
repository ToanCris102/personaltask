from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

User._meta.get_field('email')._unique = True

class Themes(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    auth_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    theme_id = models.ForeignKey(Themes, default=1, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.auth_id.email
        
