from django.contrib import admin

# Register your models here.
from .models import JobListing, Benefit, Flair



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