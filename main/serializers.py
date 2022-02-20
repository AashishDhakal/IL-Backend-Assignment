from rest_framework import serializers
from main.models import MyModel


class MyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyModel
        fields = '__all__'
