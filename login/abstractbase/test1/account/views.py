# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer
from .models import MyUser



@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if MyUser.objects.filter(email=serializer.validated_data['email']).first() is None:
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)




# from django.http import HttpResponse
# from rest_framework.parsers import JSONParser
# # Create your views here.
# def signup(request):
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         print(data)
#         return HttpResponse(status=204)

# {'username': 'aaakch@gmail.com', 'password1': 'test123!', 'password2': 'test123!', 'phone_number': '010-1234-1234', 'address': '인천광역시 부평구 이규보로61번길 123-12 100001호', 'items_of_interest': '배추, 고추, 감자, 고구마', 'job': '도매업자'}