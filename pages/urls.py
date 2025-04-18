from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),  # Ensure this exists
    path('contact/', views.contact, name='contact'),
    path('posts/', views.post_lists, name='post_list'),
    path('project-management/', views.project_management, name='project_management'),
    path('crm/', views.crm, name='crm'),
    path('employee-management/', views.employee_management, name='employee_management'),
    path('inventory/', views.inventory_management, name='inventory_management'),
    path('learning/', views.learning_platform, name='learning_platform'),
    path('communication/', views.collaboration_platform, name='collaboration_platform'),
    path('', views.home, name='home'),
]
