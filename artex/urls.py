from django.urls import path, include
from rest_framework import routers
from artex import views


router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'users')
router.register(r'profiles', views.ProfileView, 'profiles')


urlpatterns = [
    path("api/v1/", include(router.urls))
]