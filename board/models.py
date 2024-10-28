from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import pycountry

# Define a list of common tech skills manually
TECH_SKILLS_CHOICES = [
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('java', 'Java'),
    ('csharp', 'C#'),
    ('cpp', 'C++'),
    ('ruby', 'Ruby'),
    ('php', 'PHP'),
    ('swift', 'Swift'),
    ('go', 'Go'),
    ('kotlin', 'Kotlin'),
    ('typescript', 'TypeScript'),
    ('sql', 'SQL'),
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('react', 'React'),
    ('angular', 'Angular'),
    ('vue', 'Vue.js'),
    ('django', 'Django'),
    ('flask', 'Flask'),
    ('spring', 'Spring'),
    ('nodejs', 'Node.js'),
    ('express', 'Express.js'),
    ('dotnet', '.NET'),
    ('laravel', 'Laravel'),
    ('rails', 'Ruby on Rails'),
    ('docker', 'Docker'),
    ('kubernetes', 'Kubernetes'),
    ('aws', 'AWS'),
    ('azure', 'Azure'),
    ('gcp', 'GCP'),
    ('tensorflow', 'TensorFlow'),
    ('pytorch', 'PyTorch'),
    ('hadoop', 'Hadoop'),
    ('spark', 'Spark'),
    ('tableau', 'Tableau'),
    ('power_bi', 'Power BI'),
    ('jenkins', 'Jenkins'),
    ('git', 'Git'),
    ('terraform', 'Terraform'),
    ('ansible', 'Ansible'),
    ('chef', 'Chef'),
    ('puppet', 'Puppet'),
]


# Get a list of languages from pycountry
LANGUAGES_CHOICES = [(lang.alpha_2, lang.name) for lang in pycountry.languages if hasattr(lang, 'alpha_2')]
JOB_STATUS_CHOICES = [
    ('job_seeker', 'Job Seeker'),
    ('recruiter', 'Recruiter'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    nationality = CountryField(blank=True, null=True)
    country_of_residence = CountryField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    x_profile = models.URLField(blank=True, null=True)  # Assuming "X" is a social media platform
    github = models.URLField(blank=True, null=True)
    career_summary = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=50, choices=TECH_SKILLS_CHOICES, blank=True, null=True)
    languages = models.CharField(max_length=50, choices=LANGUAGES_CHOICES, blank=True, null=True)
    previous_employment = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    personal_projects = models.TextField(blank=True, null=True)
    job_status = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Benefit(models.Model):
    BENEFITS_CHOICES = [
        ('equity', 'Equity'),
        ('tuition_assistance', 'Tuition Assistance'),
        ('dental', 'Dental Insurance'),
        ('medical', 'Medical Insurance'),
        ('car', 'Car'),
        ('pension', 'Pension Contribution'),
        ('paid_leave', 'Paid Leave'),
    ]
    name = models.CharField(max_length=50, choices=BENEFITS_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class Flair(models.Model):
    FLAIRS_CHOICES = [
        ('young_team', 'Young Team'),
        ('open_office', 'Open Office'),
        ('work_from_home', 'Work from Home'),
        ('flexible_hours', 'Flexible Hours'),
        ('pet_friendly', 'Pet Friendly'),
        ('gym_on_site', 'Gym On Site'),
        ('free_snacks', 'Free Snacks'),
        ('team_outings', 'Team Outings'),
    ]
    name = models.CharField(max_length=50, choices=FLAIRS_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class JobListing(models.Model):
    EXPERIENCE_LEVEL_CHOICES = [
        ('new_grad', 'New Grad'),
        ('intermediate', 'Intermediate'),
        ('senior', 'Senior'),
    ]

    WORK_TYPE_CHOICES = [
        ('on_site', 'On Site'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
    ]

    TRAVEL_REQUIRED_CHOICES = [
        ('none', 'None'),
        ('some', 'Some'),
        ('frequent', 'Frequent'),
    ]

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contract_type = models.CharField(max_length=255)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES, default='new_grad')
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES, default='on_site')
    travel_required = models.CharField(max_length=20, choices=TRAVEL_REQUIRED_CHOICES, default='none')
    benefits = models.ManyToManyField(Benefit)
    flairs = models.ManyToManyField(Flair)

    def __str__(self):
        return self.title