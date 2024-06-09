# events/views.py
from rest_framework import viewsets
from .models import Calendar, Event
from .serializers import CalendarSerializer, EventSerializer

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
