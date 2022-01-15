from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password, check_password

from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from userapp.models.user import User
from userapp.serializers.UserSerializer import UserSerializer
from userapp.serializers.UserSerializer import UserRegistrationSerializer
from userapp.serializers.UserSerializer import UserLoginSerializer

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        hashed_pwd = make_password(request.data['password'])
        request.data['password'] = hashed_pwd
        print(request.data['password'])
        if User.objects.filter(email=request.data['email']).first():
            content = {'error': 'duplicate_error'}
            return Response(content, status=status.HTTP_409_CONFLICT)
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User registered  successfully',
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)