import os
import os.path

from django.core.management.base import BaseCommand
from django.conf import settings

from example.api.models import Photo, Employee


class Command(BaseCommand):
    sample_dir = 'samples'

    def handle(self, *args, **options):
        sample_images = [os.path.join(self.sample_dir, fn) for fn in os.listdir(os.path.join(settings.MEDIA_ROOT, self.sample_dir))]

        # employees = Employee.objects.all()
        for i, image in enumerate(sample_images):
            # post=employees[i % employees.count()]
            Photo.objects.create(image=image)
