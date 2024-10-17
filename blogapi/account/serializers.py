from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'bio', 'birth_date', 'password')  # list fields to be included in the serialized output
        extra_kwargs = {
            'password': {'write_only': True},  #  Write only means it can only be set at user creation but wont return in the API responses

        }

    def create(self, validated_data):
        # Pop(remove) the password from validated_data so we can handle it separately, by ensuring that its properly hashed
        password = validated_data.pop('password')
        
        # Create the user without a password first
        user = CustomUser.objects.create(**validated_data)
        
        # Set and hash the password properly
        user.set_password(password)
        user.save()
        
        return user #newly created user
    