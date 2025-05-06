from django.urls import path
from . import views  # This line imports all views from core/views.py

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('team/', views.team_member_list, name='team_member_list'),
    path('team/<slug:slug>/', views.team_member_detail, name='team_member_detail'),
    path('resources/', views.resource_list, name='resource_list'),
    path('resources/<slug:slug>/', views.resource_detail, name='resource_detail'),
    path('inquiries/', views.inquiry_list, name='inquiry_list'),
    path('active-projects/', views.active_project_list, name='active_project_list'),
    path('active-projects/<slug:slug>/', views.active_project_detail, name='active_project_detail'),
    # Add any other URLs for your 'core' app hereAdd this line for the root path
]