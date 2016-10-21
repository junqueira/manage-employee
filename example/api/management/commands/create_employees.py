from django.core.management.base import BaseCommand

from example.api.models import Department, Employee, User, Photo


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        departments = Department.objects.all()
        photos = Photo.objects.all()
        employees = ['Bob', 'Sally', 'Joe', 'Rachel', 'John']
        descriptions = ['This is a great employee',
                        'Another thing I wanted to share',
                        'other',
                        'this employes not work',
                        '...']

        for index, employee in enumerate(employees):
            # import ipdb; ipdb.set_trace()
            Employee.objects.create(author=users[index % users.count()],
                                    department=departments[index % departments.count()],
                                    photo=photos[index % photos.count()],
                                    name=employee,
                                    email="{}@example.com".format(employees[index].lower()),
                                    description=descriptions[index])