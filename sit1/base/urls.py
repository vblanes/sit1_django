from django.urls import path

from . import views

urlpatterns = [
    path('', views.data_input, name='data_input'),
    path('send_test_job', views.send_test_job, name='send_test_job'),
]