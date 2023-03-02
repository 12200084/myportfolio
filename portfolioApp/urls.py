from django.urls import path
from . import views

app_name = 'portfolioApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:project_id>/', views.projectDetial, name='projectDetail'),
]
