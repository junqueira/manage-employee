from django.core.management.base import BaseCommand

from example.api.models import Department


class Command(BaseCommand):
    def handle(self, *args, **options):
        departments = ['Operation', 'Development', 'Arquiteture', 'Test', 'Manager']
        for department in departments:
            Department.objects.create(name=department.lower())
