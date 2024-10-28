from django.core.management.base import BaseCommand
from faker import Faker
from board.models import JobListing, Benefit, Flair
import random

class Command(BaseCommand):
    help = 'Create fake job listings'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Get all benefits and flairs
        benefits = list(Benefit.objects.all())
        flairs = list(Flair.objects.all())

        for _ in range(20):  # Create 20 fake job listings
            job = JobListing.objects.create(
                title=fake.job(),
                company=fake.company(),
                location=fake.city(),
                contract_type=random.choice(['Full-time', 'Part-time', 'Contract']),
                description=fake.text(),
                application_deadline=fake.date_time_this_year(),
                salary=fake.random_number(digits=5),
                experience_level=random.choice(['new_grad', 'intermediate', 'senior']),
                work_type=random.choice(['on_site', 'remote', 'hybrid']),
                travel_required=random.choice(['none', 'some', 'frequent']),
            )
            # Add random benefits and flairs
            job.benefits.set(random.sample(benefits, k=random.randint(1, len(benefits))))
            job.flairs.set(random.sample(flairs, k=random.randint(1, len(flairs))))
            job.save()

        self.stdout.write(self.style.SUCCESS('Successfully created fake job listings'))