from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crime-statistics/<str:country_name>/', views.get_country_crime),
    path('map-page/', views.map_page, name='map-page'),
    path('upload_dataset/', views.upload_dataset_view, name='upload_dataset'),
    path('get_country_stats/', views.get_country_stats, name='get_country_stats'),
    path('statsPage/', views.stats_page_view, name='statsPage'),
    path('report/', views.report, name='report'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('stats/', views.stats, name='stats'),
]
