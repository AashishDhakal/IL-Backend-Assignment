from django.shortcuts import render
from rest_framework.views import APIView
from main.models import MyModel
from main.helpers import parse_search_phrase
from rest_framework.response import Response
from main.api.v1.serializers import MyModelSerializer
from rest_framework.status import HTTP_200_OK

# Create your views here.


class FilterAPIView(APIView):

    def get(self, request, *args, **kwargs):
        search_phrase = self.request.query_params.get('search_phrase')
        if search_phrase:
            allowed_fields = ['date', 'distance']
            query = parse_search_phrase(allowed_fields, search_phrase)
            queryset = MyModel.objects.filter(query)
        else:
            queryset = MyModel.objects.all()
        return Response(status=HTTP_200_OK, data={
            'data': MyModelSerializer(queryset, many=True).data
        })
