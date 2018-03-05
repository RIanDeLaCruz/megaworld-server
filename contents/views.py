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
                ('number', '09178831588')
        )

        path = 'https://semaphore.co/api/v4/messages?' + urllib.parse.urlencode(params)
        requests.post(path)

        return Response({'success', True, 'message', message}, status=status.HTTP_200_OK)

class ProjectView(APIView):
    def get(self, request):
        path = 'http://megaworldlifestylecondos.com/wp-json/wp/v2/mw_project'
        r = requests.get(path)

        data = r.json()
        names = [project['title']['rendered'] for project in data]
        ids = [project['id'] for project in data]

        print(data[0]['acf']['unit_layout'][0]['unit_layout_name'])

        projects = [{
                'id': project['id'],
                'title': project['title']['rendered'],
                'status': 'Preselling' if 6 in project['categories'] else 'Ready',
                'unit_layouts': [layout.get('unit_layout_name') for layout in
                    project['acf'].get('unit_layout')],
                'location': project['acf'].get('location'),
                'link': project['link']
            } for project in data
        ]

        project_query = request.GET.get('unit_type')
        status_query = request.GET.get('status')

        if project_query != None or status_query != None:
            projects = [
                project for project in projects
                if project['status'] == status_query and
                project_query in project['unit_layouts']
            ]

        return Response(projects, status=status.HTTP_200_OK)
