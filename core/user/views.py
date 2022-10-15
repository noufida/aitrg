from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework  import status
from .models import Account
from .serializer import AccountSerializer

#  admin register   view

@api_view(['POST'])
def admin_register(request):

    try:
        data=request.data
        name=data['name']
        username=data['username']
        email=data['email']
        password=data['password']
        confirm_password=data['confirm_password']

        # validatations for blank
        if email==''  or password=='' or confirm_password=='':
            message={'error':'Required fields '}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

        # validation for password matching
        elif password!=confirm_password:
            message={'error':'Passwords does not match'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

        # for password length check
        elif len(password)<6:
            message={'error':'Password should contain min 6 charecter'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        
        # checking the email is already exist or not
        elif Account.objects.filter(email=email).exists():
            message={'error':'Email already exist'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
            
        # creating a object of Account model for signup 
        user=Account.objects.create(
            name=name,
            username=username,
            email=email,
            password=make_password(password),                   
        )
        serializer = AccountSerializer(user,many=False)
        return Response(serializer.data)

    except:
        message={'error':'Some error occured'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)