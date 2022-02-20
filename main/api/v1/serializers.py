from rest_framework import serializers
from main.models import MyModel


class MyModelSerializer(serializers.ModelSerializer):
    model = MyModel
    fields = '__all__'
