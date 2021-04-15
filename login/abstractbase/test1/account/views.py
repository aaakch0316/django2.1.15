from django.contrib.auth import get_user_model

# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer, UserSerializer
from .models import MyUser


User = get_user_model()


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



# login
from .serializers import UserLoginSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        # print(request.data)
        serializer = UserLoginSerializer(data=request.data)
        # print(serializer)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'success': 'True',
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)


# from django.http import HttpResponse
# from rest_framework.parsers import JSONParser
# # Create your views here.
# def signup(request):
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         print(data)
#         return HttpResponse(status=204)

# {'username': 'aaakch@gmail.com', 'password1': 'test123!', 'password2': 'test123!', 'phone_number': '010-1234-1234', 'address': '인천광역시 부평구 이규보로61번길 123-12 100001호', 'items_of_interest': '배추, 고추, 감자, 고구마', 'job': '도매업자'}

'''
로그인 로그아웃 과정 (token authentication)

1. 화면에서 사용자가 email, password를 입력을 한다.

2. 사용자가 입력한 email, password 를 서버로 보낸다.

3. Email, password 가 맞다면 고유한 TOKEN을 발행한다.

4. 발행된 토큰을 response로 보낸다 (browser).

5. 토큰을 클라이언트 어딘가에 저장해 놓는다. (cookie or session)

6. 다른 API를 사용할 때마다 header에 TOKEN을 같이 서버에 보낸다.

7. 서버는 TOKEN 을 확인해서 token 이 valid 한지 확인한 뒤 response를 보낸다.

8. 로그아웃은 토큰을 지우는 것과 같다.
'''
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view


# @api_view(['GET'])
# def user_list(request):
#     queryset = MyUser.objects.all()
#     print(queryset)
#     serializer = UserSerializer(queryset, many=True) # many=True를 안하면 is_valid() 하라고 뜬다.
#     # serializer.is_valid(raise_exception=True)
#     print(serializer)
#     print('--------------------------')
#     print(serializer.data)
#     # json_render = JSONRenderer()
#     # user_json = json_render.render(serializer.data)
#     # print('--------------------------')
#     # print(user_json)
#     # return JsonResponse(serializer.data)
#     return HttpResponse()


# '''
# 쿼리셋이나 특정 타입을 JSON으로 곧장 변환시킬 수 없습니다.
# 다음과 같이 django.core의 serializers를 사용해서 쿼리셋을 json화 해준 후 HttpResponse에 담아서 리턴해야 json을 받을 수 있다.
# 물론 이 방법은 잘 작동하지만 데이터에 대한 validation을 하지 않는다는 단점이 있다.
# '''
from django.core import serializers
# def user_list(request):
#     queryset = MyUser.objects.all()
#     data = serializers.serialize("json", queryset) 
#     return HttpResponse(content=data)


from rest_framework.response import Response
from .serializers import BaseSerializer, UserSerializer, MetaUserSerializer

from rest_framework.decorators import authentication_classes, permission_classes
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def user_list(request):
    queryset = MyUser.objects.all()
    serialized_data = MetaUserSerializer(queryset, many=True) 
    return Response(data=serialized_data.data)


# @api_view(['GET'])
# @authentication_classes([])
# @permission_classes([])
# def user_list(request):
#     queryset = MyUser.objects.all()
#     serialized_data = MetaUserSerializer(queryset, many=True) 
#     return JsonResponse(serialized_data.data, safe=False)
