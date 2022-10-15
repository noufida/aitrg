from rest_framework import serializers
from . models import Account


# Account serializer for account json response
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields="__all__"