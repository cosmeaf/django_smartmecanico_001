from django.contrib.auth.models import User
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ('username', 'password',)
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only': True}
        }

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class SendEmailResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

    def validate(self, attrs):
        # try:
        #     email = attrs.get('email', '')
        #     user = user.objects.get(email=email)
        #     token = '1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik!@#$%!QSW@#E'
        #     current_site = get_current_site().domain
        #     relativeLink = reverse('email-verify')
        #     absurl = 'http://' + current_site + \
        #         relativeLink + '?token'+str(token)
        #     pass
        # except exprexion as identifier:
        #     pass
        return 'recovery email'
