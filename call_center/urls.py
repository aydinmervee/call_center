from django.urls import path

from call_center.views import get_call_center_data

urlpatterns = [
    path('', get_call_center_data, name='index'),
]
