from django.urls import path
from .views import EventListView, CalendarListView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('calendars/', CalendarListView.as_view(), name='calendar-list'),
]
