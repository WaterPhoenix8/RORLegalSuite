from django.urls import path

from . import views

"""
urlpatterns = [
    path('', views.cases, name='cases')
]
"""

urlpatterns = [
    path('', views.index, name='index')
]