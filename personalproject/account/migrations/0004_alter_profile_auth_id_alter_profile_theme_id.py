# Generated by Django 4.0.5 on 2022-06-23 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_alter_profile_theme_id_alter_profile_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='auth_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='theme_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.theme'),
        ),
    ]
