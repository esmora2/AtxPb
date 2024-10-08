from django.urls import path, include
from rest_framework import routers
from artex import views


router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'users')
router.register(r'profiles', views.ProfileView, 'profiles')
router.register(r'cexquotes', views.CexQuotesView, 'cexquotes')
router.register(r'cexplan', views.CexPlanView, 'cexplan')
router.register(r'cexstand', views.CexStandView, 'cexstand')
router.register(r'cexcategory', views.CexCategoryView, 'cexcategory')

urlpatterns = [
    path("api/v1/", include(router.urls))
]