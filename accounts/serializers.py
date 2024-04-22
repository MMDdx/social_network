from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')

        extra_kwargs = {'first_name': {'required': False}, 'last_name': {'required': False}}

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'does not match!!'})
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'],
                                        first_name=validated_data.get('first_name', ''),
                                        last_name=validated_data.get('last_name', ''),
                                        password=validated_data['password1'])

        return user
