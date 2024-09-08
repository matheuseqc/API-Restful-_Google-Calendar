from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from .filters import TaskFilter  

import os
from decouple import config
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_google_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            client_id = config('GOOGLE_CLIENT_ID')
            client_secret = config('GOOGLE_CLIENT_SECRET')
            auth_uri = config('GOOGLE_AUTH_URI')
            token_uri = config('GOOGLE_TOKEN_URI')
            auth_provider_x509_cert_url = config('GOOGLE_AUTH_PROVIDER_X509_CERT_URL')
            redirect_uris = config('GOOGLE_REDIRECT_URIS').split(',')

            flow = InstalledAppFlow.from_client_config({
                "installed": {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "auth_uri": auth_uri,
                    "token_uri": token_uri,
                    "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
                    "redirect_uris": redirect_uris
                }
            }, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter

    def perform_create(self, serializer):
        task = serializer.save()
        service = get_google_service()
        event = {
            'summary': task.title,
            'description': task.description,
            'start': {
                'dateTime': f'{task.date}T{task.time}',
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': f'{task.date}T{task.time}',
                'timeZone': 'UTC',
            },
        }
        created_event = service.events().insert(calendarId='primary', body=event).execute()
        task.google_event_id = created_event['id']
        task.save()

    def perform_destroy(self, instance):
        service = get_google_service()
        if hasattr(instance, 'google_event_id') and instance.google_event_id:
            try:
                service.events().delete(calendarId='primary', eventId=instance.google_event_id).execute()
            except Exception as e:
                print(f'An error occurred while deleting the event: {e}')
        instance.delete()
