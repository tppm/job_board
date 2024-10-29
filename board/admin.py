from django.contrib import admin

# Register your models here.
from .models import JobListing, Benefit, Flair, UserProfile, Language, Skill





@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Flair)
class FlairAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_date', 'application_deadline', 'salary', 'experience_level', 'work_type', 'travel_required')
    list_filter = ('experience_level', 'work_type', 'travel_required', 'benefits', 'flairs')
    search_fields = ('title', 'company', 'location', 'description')
    filter_horizontal = ('benefits', 'flairs')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nationality', 'country_of_residence')
    search_fields = ('user__username', 'nationality', 'country_of_residence')
    list_filter = ('nationality', 'country_of_residence')
    fieldsets = (
        (None, {
            'fields': ('user', 'profile_picture', 'nationality', 'country_of_residence', 'linkedin', 'x_profile', 'github', 'career_summary', 'skills', 'languages', 'previous_employment', 'education', 'personal_projects')
        }),
    )