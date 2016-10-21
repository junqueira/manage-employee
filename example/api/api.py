from rest_framework import generics, permissions


from .serializers import UserSerializer, DepartmentSerializer, EmployeeSerializer, PhotoSerializer
from .models import User, Department, Employee, Photo
from .permissions import EmployeeAuthorCanEditPermission


class UserEmployeeList(generics.ListAPIView):
    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = super(UserEmployeeList, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


class UserMixin(object):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(UserMixin, generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(UserMixin, generics.RetrieveAPIView):
    lookup_field = 'username'


class DepartmentMixin(object):
    model = Department
    queryset = Department.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [
        EmployeeAuthorCanEditPermission
    ]

    def perform_create(self, serializer):
        """Force author to the current user on save"""
        serializer.save(author=self.request.user)

class DepartmentList(DepartmentMixin, generics.ListCreateAPIView):
    pass


class DepartmentDetail(DepartmentMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class EmployeeMixin(object):
    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [
        EmployeeAuthorCanEditPermission
    ]

    def perform_create(self, serializer):
        """Force author to the current user on save"""
        serializer.save(author=self.request.user)


class EmployeeList(EmployeeMixin, generics.ListCreateAPIView):
    pass


class EmployeeDetail(EmployeeMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class EmployeePhotoList(generics.ListAPIView):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = super(EmployeePhotoList, self).get_queryset()
        return queryset.filter(photos__pk=self.kwargs.get('pk'))


class PhotoMixin(object):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoList(PhotoMixin, generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class PhotoDetail(PhotoMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.AllowAny
    ]