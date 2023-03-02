from django.shortcuts import render
from .models import myproject, herosection, projectcount, copyright, serviceoffer, skills, maplocation,learing_resource,socialmedia_link
from django.http import HttpResponse

# Create your views here.


def home(request):
    herosection_list = herosection.objects.all()
    project_list = myproject.objects.all()
    projectcount_list = projectcount.objects.all()
    serviceoffer_list = serviceoffer.objects.all()
    skill_list = skills.objects.all()
    copyright_list = copyright.objects.all()
    present_location = maplocation.objects.all()
    learing_list = learing_resource.objects.all()
    social_meadia = socialmedia_link.objects.all()


    context = {
        'herosection_list': herosection_list,
        'project_list': project_list,
        'skill_list': skill_list,
        'projectcount_list': projectcount_list,
        'serviceoffer_list': serviceoffer_list,
        'copyright_list': copyright_list,
        'present_location': present_location,
        'learing_list': learing_list,
        'social_meadia':social_meadia,
    }
    return render(request, 'home.html', context)


def projectDetial(request, project_id):
    project = myproject.objects.get(pk=project_id)
    context = {
        'project': project,
    }
    return render(request, 'detail.html', context)
