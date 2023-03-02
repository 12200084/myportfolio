from django.urls import path
from . import views

app_name = 'portfolioApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:project_id>/', views.projectDetial, name='projectDetail'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)