from django.urls import path
from . import views

app_name = 'studentpages'
urlpatterns = [
    path('', views.index, name='index'),
    path('students/',views.students, name='students'),
]
