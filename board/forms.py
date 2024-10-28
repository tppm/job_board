from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_picture', 'nationality', 'country_of_residence', 'linkedin', 'x_profile', 'github',
            'career_summary', 'skills', 'languages', 'previous_employment', 'education', 'personal_projects', 'job_status'
        ]
        widgets = {
            'career_summary': forms.Textarea(attrs={'rows': 3}),
            'previous_employment': forms.Textarea(attrs={'rows': 3}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'personal_projects': forms.Textarea(attrs={'rows': 3}),
        }