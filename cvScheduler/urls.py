from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('schedule/', views.schedule, name='schedule'),
    path('<int:id>/', views.resume, name='resume'),
    path('vprofile/<id>/', views.view_profile, name='viewprofile'),
    path('view/', views.viewSchedule, name='view_schedule'),
    path('delete_schedule/<id>/', views.delete_schedule, name='delete_schedule'),
    path('update_schedule/<id>/', views.update_schedule, name='update_schedule'),

]
