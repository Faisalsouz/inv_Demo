from django.urls import path
from demo_app import views

urlpatterns=[path('',views.home,name='main'),
             path('scraper',views.scraper_main,name='demo_main'),
             path('instructions',views.how_to,name='how'),
             path('new_run',views.scraper_main,name='new_run'),
             path('old_run',views.scraper_main,name='old_run'),
             path('zip_files', views.download_zip, name='getzip'),
             ] #you need to give name of functionpath("<int:pk>/", views.project_detail, name="project_detail")
