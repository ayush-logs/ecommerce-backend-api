# TODO add JWT blacklisting view

from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
