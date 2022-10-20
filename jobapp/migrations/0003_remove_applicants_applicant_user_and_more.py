# Generated by Django 4.1.2 on 2022-10-19 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobapp', '0002_alter_job_applicants_alter_job_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicants',
            name='applicant_user',
        ),
        migrations.RemoveField(
            model_name='job',
            name='applicants',
        ),
        migrations.AddField(
            model_name='applicants',
            name='job',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='jobapp.job'),
        ),
        migrations.AddField(
            model_name='applicants',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]