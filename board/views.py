from django.shortcuts import render, get_object_or_404, redirect
from .models import JobListing
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import UserProfile
from .forms import UserProfileForm, JobPostingForm

def job_listings(request):
    query = request.GET.get('q')
    if query:
        jobs = JobListing.objects.filter(
            Q(title__icontains=query) |
            Q(company__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        jobs = JobListing.objects.all()
    return render(request, 'board/job_listings.html', {'jobs': jobs})

def job_details(request, id):
    job = get_object_or_404(JobListing, id=id)
    return render(request, 'board/job_details.html', {'job': job})

def about(request):
    return render(request, 'board/about.html')

def contact(request):
    return render(request, 'board/contact.html')


@login_required
def profile(request):
    user = request.user
    if not hasattr(user, 'userprofile'):
        UserProfile.objects.create(user=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user.userprofile)
    return render(request, 'board/profile.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_listings')
    else:
        form = UserCreationForm()
    return render(request, 'board/signup.html', {'form': form})


@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save()
            return redirect('job_details', id=job.id)
    else:
        form = JobPostingForm()
    return render(request, 'board/post_job.html', {'form': form})