from rest_framework import viewsets
from .serializer import UserSerializer, ProfileSerializer, CexQuotesSerializer, CexPlanSerializer
from .models import User, Profile, CexQuotes, CexPlan


# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class CexQuotesView(viewsets.ModelViewSet):
    serializer_class = CexQuotesSerializer
    queryset = CexQuotes.objects.all()

class CexPlanView(viewsets.ModelViewSet):
    serializer_class = CexPlanSerializer
    queryset = CexPlan.objects.all()