from rest_framework import exceptions

from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import User
from .serializers import UserSerializer


# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match!')

        # need to build more testing into this
        # data['is_ambassador'] = 'api/ambassador' in request.path
        data['is_ambassador'] = 0

        serializer =  UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        print(user)

        if user is None:
            raise exceptions.AuthenticationFailed('User does not exist')
        # eventually hide these dont alert use to 
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid credentials')

        return Response(UserSerializer(user).data)
        # scope = 'ambassador' if 'api/ambassador' in request.path else 'admin'

