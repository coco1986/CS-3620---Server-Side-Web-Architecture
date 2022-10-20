from . import views
from django.urls import path

app_name = 'madlibs'
urlpatterns = [
    path('', views.index, name="index"),
    path('madlib/', views.madlib, name="madlib")
]

