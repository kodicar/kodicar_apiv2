from rest_framework import serializers
from . models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id",'username', 'first_name', 'last_name', 'email', 'avatar',  'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validated_first_name(self, value):
        return value.upper()

    def create(self, validated_data):
        user = Profile(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)

        return user