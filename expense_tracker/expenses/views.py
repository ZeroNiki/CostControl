from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema 
 
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Transaction
from .serializers import CategorySerializers, TransactionSerializers, UserRegistrationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializers 
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend] 
    filter_fields = ["category", "date"]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserRegistrationViewSet(APIView):
    permission_classes = [permissions.AllowAny]  # Доступ для всех пользователей

    @extend_schema(
        request=UserRegistrationSerializer,
        responses={201: UserRegistrationSerializer},
        description="Register a new user",
        tags=["Authentication"]
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "Message": "User registered successfully!",
                "Refresh": str(refresh),
                "Access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
