from django.contrib.auth import Group ,User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        Model = Group
        fields = ['url','name']        