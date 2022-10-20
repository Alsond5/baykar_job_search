from django import forms

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

class AddJob(forms.Form):
    title = forms.CharField(max_length=255)
    department = forms.CharField(max_length=150)
    country = forms.ChoiceField(choices=COUNTRY, max_length=255, blank=False)
    status = forms.ChoiceField(choices=WAY_OF_WORKING, max_length=255, default=0)
    description = forms.CharField(widget=forms.Textarea)
    require_skills = forms.CharField(required=False)
    