# auth_api_views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from sellerapp.models import Seller
from .serializers import SignupSerializer


# =========================
# SIGNUP API (CLEAN)
# =========================

@api_view(['POST'])
def signup_api(request):

    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        image = request.FILES.get('image')

        Seller.objects.create(
            user=user,
            shop_name=f"{user.username}'s Shop",
            phone="",
            image=image
        )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "success": True,
            "message": "Account created successfully",
            "token": token.key,
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# LOGIN API
# =========================

@api_view(['POST'])
def login_api(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if not user:
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        "success": True,
        "token": token.key,
        "username": user.username,
        "email": user.email
    })


# =========================
# LOGOUT API (SAFE FIX)
# =========================

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_api(request):

    try:
        request.user.auth_token.delete()
    except:
        pass

    return Response({
        "success": True,
        "message": "Logout successful"
    })