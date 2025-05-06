from django.shortcuts import render
from .models import Project, TeamMember, Resource, Inquiry, ActiveProject
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
     return render(request, 'core/home.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'core/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})

def team_member_list(request):
    team_members = TeamMember.objects.all()
    return render(request, 'core/team_member_list.html', {'team_members': team_members})

def team_member_detail(request, slug):
    team_member = TeamMember.objects.get(slug=slug)
    return render(request, 'core/team_member_detail.html', {'team_member': team_member})

def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'core/resource_list.html', {'resources': resources})

def resource_detail(request, slug):
    resource = Resource.objects.get(slug=slug)
    return render(request, 'core/resource_detail.html', {'resource': resource})

def inquiry_list(request):
    inquiries = Inquiry.objects.all().order_by('-submitted_at')
    return render(request, 'core/inquiry_list.html', {'inquiries': inquiries})

def active_project_list(request):
    active_projects = ActiveProject.objects.all()
    return render(request, 'core/active_project_list.html', {'active_projects': active_projects})

def active_project_detail(request, slug):
    active_project = ActiveProject.objects.get(slug=slug)
    return render(request, 'core/active_project_detail.html', {'active_project': active_project})
