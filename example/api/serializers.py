from rest_framework import serializers

from .models import User, Department, Employee, Photo


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField(view_name='useremployee-list', lookup_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts', )

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department

class EmployeeSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    photos = serializers.HyperlinkedIdentityField(view_name='employeephoto-list')
    # author = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username')

    def get_validation_exclusions(self, *args, **kwargs):
        # Need to exclude `user` since we'll add that later based off the request
        exclusions = super(EmployeeSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['author']

    class Meta:
        model = Employee


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')

    class Meta:
        model = Photo
