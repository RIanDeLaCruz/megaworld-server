from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import datetime
import secrets
import sys, urllib


class ChikkaView(APIView):
    def post(self, request):

        api_key = 'b30ae54fd061de0faa02582e765b52a8'

        message = "From {}:\n\
        Regarding: {} \n\
        {}".format(request.POST['contact_number'], request.POST['property'], request.POST['message'])
        print ( message )

        params = (
                ('apikey', api_key),
                ('message', message),
                ('number', '09267398210')
        )

        path = 'https://semaphore.co/api/v4/messages?' + urllib.parse.urlencode(params)
        requests.post(path)

        return Response({'success', True, 'message', message}, status=status.HTTP_200_OK)
