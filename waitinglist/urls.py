from django.urls import path
from . views import WaitingListView


urlpatterns = [
    path('waitinglist/', WaitingListView.as_view(), name='waitinglist'),
]