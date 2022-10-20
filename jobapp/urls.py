from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<slug:slug>-<int:id>', views.jobdetails, name='jobdetails'),
    path('apply/<int:id>', views.apply, name='apply'),
]