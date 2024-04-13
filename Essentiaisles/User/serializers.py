from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name')
        extra_kwargs = {'password':{'write_only': True}}