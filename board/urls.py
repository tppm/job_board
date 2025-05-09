from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_listings, name='job_listings'),
    path('jobs/<int:id>/', views.job_details, name='job_details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('jobs/post/', views.post_job, name='post_job')
]