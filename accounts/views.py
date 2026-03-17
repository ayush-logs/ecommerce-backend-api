# TODO add JWT blacklisting view

from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):
    def post(self, request):
        token = RefreshToken(token=request.data["refresh"])
        token.blacklist()
        return Response({"detail": "Logged Out."})
