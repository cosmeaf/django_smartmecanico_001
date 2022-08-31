from django.contrib.auth.models import User
from rest_framework import serializers

# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


# class UserAllSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

#     def create(self, validated_data):
#         user = User(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User

#     def to_representation(self, instance):
#         # data = super().to_representation(instance)
#         # return data
#         return {
#             'id': instance['id'],
#             'username': instance['username'],
#             'email': instance['email'],
#             'first_name': instance['first_name'],
#             'last_name': instance['last_name'],
#             'password': instance['password']
#         }
