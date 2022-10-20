from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Applicants
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {

    }

    if request.method == 'POST':
        search = request.POST['search']
        if search:
            skills = []

            if search.find(','):
                for x in search.split(','):
                    skills.append(x.strip())
            else:
                skills.append(search)

            query = Job.objects.filter(require_skills__overlap=skills)
            context['search'] = skills
    else:
        query = Job.objects.order_by('-created_on')

    template_name = 'pages/index.html'

    context['jobs'] = query

    return render(request, template_name, context)

def jobdetails(request, slug, id, message=None):
    template_name = 'pages/detail.html'
    query = Job.objects.get(slug=slug, id=id)

    is_applied = False

    if request.user.is_authenticated:
        is_applied = Applicants.objects.filter(user=request.user, job=query).exists()

    context = {
        'job': query,
        'message': message,
        'is_applied': is_applied,
    }

    return render(request, template_name, context)

@login_required(login_url='/account/login')
def apply(request, id):
    if Job.objects.filter(id=id).exists():
        job = Job.objects.get(id=id)
        user = request.user

        if Applicants.objects.filter(user=user, job=job).exists():
            return jobdetails(request, job.slug, job.pk, 'You\'ve already applied this job')
        else:
            Applicants.objects.create(user=user, job=job)

            return jobdetails(request, job.slug, job.pk, 'Your application has been received')
    else:
        return HttpResponse('Invalid job id')

