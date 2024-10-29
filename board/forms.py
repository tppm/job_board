from django import forms
from .models import UserProfile, Language, Skill, JobListing
from django_countries.widgets import CountrySelectWidget
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



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'job_status', 'nationality', 'country_of_residence', 'languages', 'skills', 'profile_picture',
            'linkedin', 'x_profile', 'github', 'career_summary', 'previous_employment', 'education', 'personal_projects'
        ]
        widgets = {
            'nationality': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'country_of_residence': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'languages': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'career_summary': forms.Textarea(attrs={'rows': 3}),
            'previous_employment': forms.Textarea(attrs={'rows': 3}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'personal_projects': forms.Textarea(attrs={'rows': 3}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-populate language choices
        language_choices = [(lang.code, lang.name) for lang in Language.objects.all()]
        if not Language.objects.exists():
            # Create default languages if none exist
            for code, name in LANGUAGES_CHOICES:
                Language.objects.create(code=code, name=name)
            language_choices = [(lang.code, lang.name) for lang in Language.objects.all()]
        self.fields['languages'].choices = language_choices

        # Pre-populate skill choices
        skill_choices = [(skill.code, skill.name) for skill in Skill.objects.all()]
        if not Skill.objects.exists():
            # Create default skills if none exist
            for code, name in TECH_SKILLS_CHOICES:
                Skill.objects.create(code=code, name=name)
            skill_choices = [(skill.code, skill.name) for skill in Skill.objects.all()]
        self.fields['skills'].choices = skill_choices





class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = [
            'title', 'company', 'company_logo', 'location', 'contract_type',
            'description', 'application_deadline', 'salary', 'experience_level',
            'work_type', 'travel_required', 'benefits', 'flairs'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'application_deadline': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'benefits': forms.CheckboxSelectMultiple(),
            'flairs': forms.CheckboxSelectMultiple(),
        }