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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, related_name = 'user_info')
    birthday = models.DateField()
    phone = models.CharField(max_length = 11, blank=False)
    country = models.CharField(choices=COUNTRY, max_length=255, blank=False)
    slug = models.SlugField(max_length=150, unique=True)
    cv = models.FileField(upload_to='CVs', blank=False)
    school = models.CharField(max_length = 255, blank=False)
    graduate_year = models.PositiveIntegerField()
    skills = ArrayField(models.CharField(max_length=250), blank=True)
    status = models.CharField(choices=WAY_OF_WORKING, max_length=255, default=0)

    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)
    
    def __str__(self):
        return self.user.username