from django.conf.urls import url, include

from .api import UserList, UserDetail
# from .api import DepartmentList, DepartmentDetail
from .api import EmployeeList, EmployeeDetail, UserEmployeeList
from .api import PhotoList, PhotoDetail, EmployeePhotoList

user_urls = [
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/employees$', UserEmployeeList.as_view(), name='useremployee-list'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
]

employee_urls = [
    url(r'^/(?P<pk>\d+)/photos$', EmployeePhotoList.as_view(), name='employeephoto-list'),
    url(r'^/(?P<pk>\d+)$', EmployeeDetail.as_view(), name='employee-detail'),
    url(r'^$', EmployeeList.as_view(), name='employee-list')
]

photo_urls = [
    url(r'^/(?P<pk>\d+)$', PhotoDetail.as_view(), name='photo-detail'),
    url(r'^$', PhotoList.as_view(), name='photo-list')
]

urlpatterns = [
    url(r'^users', include(user_urls)),
    url(r'^employees', include(employee_urls)),
    url(r'^photos', include(photo_urls)),
]
