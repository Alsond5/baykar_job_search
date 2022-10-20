from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

WAY_OF_WORKING = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Intern', 'Intern'),
    ('Remote', 'Remote')
)

COUNTRY = (
    ('Turkey', 'Turkey'),
    ('Others', 'Others')
)

class Job(models.Model):
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=150)
    country = models.CharField(choices=COUNTRY, max_length=255, blank=False)
    status = models.CharField(choices=WAY_OF_WORKING, max_length=255, default=0)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    require_skills = ArrayField(models.CharField(max_length = 250))
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Applicants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default=None)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job', default=None)

    def __str__(self):
        return self.user.username