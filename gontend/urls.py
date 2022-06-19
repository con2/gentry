from django.urls import path

from gontend.views import dashboard, status

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('healthz', status, name='status'),
]
