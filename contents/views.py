from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import datetime
import sys, urllib


class ChikkaView(APIView):
    def post(self, request):

        api_key = 'b30ae54fd061de0faa02582e765b52a8'

        message = "From {}, {}:\n\
        Regarding: {} \n\
        {}".format(request.POST['contact_number'], request.POST['name'],
                request.POST['property'], request.POST['message'])
        print ( message )

        params = (
                ('apikey', api_key),
                ('message', message),
                ('number', '09267398210')
        )

        path = 'https://semaphore.co/api/v4/messages?' + urllib.parse.urlencode(params)
        requests.post(path)

        return Response({'success', True, 'message', message}, status=status.HTTP_200_OK)

class ProjectView(APIView):
    def get(self, request):
        path = 'http://megaworldlifestylecondos.com/wp-json/wp/v2/mw_project'
        r = requests.get(path)

        query_strings = request.GET.urlencode().split('&')

        data = r.json()
        names = [project['title']['rendered'] for project in data]
        ids = [project['id'] for project in data]

        projects = [{
                'id': project['id'],
                'title': project['title']['rendered'],
                'acf': project['acf'],
                'status': 'Preselling' if 6 in project['categories'] else 'Ready'
            } for project in data
        ]

        project_query = urllib.parse.unquote_plus([
            item for item in query_strings if 'project' in item
        ][0].split('=')[1])

        status_query = urllib.parse.unquote_plus([
            item for item in query_strings if 'status' in item
        ][0].split('=')[1])

        projects = [
            project for project in projects
            if project['title'] == project_query or
            project['status'] == status_query
        ]

        return Response(projects, status=status.HTTP_200_OK)
