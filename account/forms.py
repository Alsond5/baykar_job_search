from django import forms
from .models import Profile

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

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthday', 'phone', 'country', 'cv', 'school', 'graduate_year', 'skills', 'status')
