from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

#
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSets Version 1
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @api_view(['GET', 'POST'])
# def user_api_view(request):
#     """
#     APIView Version 2
#     """
#     if request.method == 'GET':
#         users = User.objects.all().values('id', 'username', 'email',
#                                           'password', 'first_name', 'last_name')
#         users_serializer = UserListSerializer(users, many=True)
#         return Response(users_serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
#         users_serializer = UserAllSerializer(data=request.data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return Response(users_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(users_serializer.data, status=status.HTTP_404_NOT_FOUND)

#     return Response(users_serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def user_api_view_detail(request, pk=None):
#     """
#     APIView Version 2
#     """
#     user = User.objects.filter(id=pk).first()
#     if user:
#         if request.method == 'GET':
#             user_serializer = UserListSerializer(user)
#             return Response(user_serializer.data, status=status.HTTP_200_OK)

#         elif request.method == 'PUT':
#             user_serializer = UserListSerializer(user, data=request.data)
#             if user_serializer.is_valid():
#                 user_serializer.save()
#                 return Response(user_serializer.data, status=status.HTTP_200_OK)
#             return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == 'DELETE':
#             user.delete()
#             return Response({'message': 'user successfully deleted'}, status=status.HTTP_204_NO_CONTENT)

#         return Response(user_serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     return Response({'message': 'User not Found'}, status=status.HTTP_404_NOT_FOUND)
