# Generated by Django 4.0.5 on 2022-06-20 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_rename_priority_task_priority_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task.status'),
        ),
    ]
