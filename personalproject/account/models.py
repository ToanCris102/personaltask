from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

User._meta.get_field('email')._unique = True

class Theme(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    auth_id = models.OneToOneField(User, related_name='profiles', on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True, blank=True)
    theme_id = models.ForeignKey(Theme, related_name='profiles', default=1, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.auth_id
