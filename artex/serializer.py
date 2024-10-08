from rest_framework import serializers
from .models import User, Profile, CexQuotes, CexPlan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CexQuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CexQuotes
        fields = '__all__'

class CexPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CexPlan
        fields = '__all__'