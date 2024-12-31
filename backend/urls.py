from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),



    # authentication urls

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/<str:referal>', views.refer_register, name='referal'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)