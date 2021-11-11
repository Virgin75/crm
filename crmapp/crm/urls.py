from django.urls import path, include
from django.conf.urls import url
from .views import ClientDetail, ListCreateClient, ListCreateContract, ContractDetail, ListCreateEvent, EventDetail

urlpatterns = [
    path('clients/<int:pk>', ClientDetail.as_view()),
    path('clients', ListCreateClient.as_view()),
    path('contracts', ListCreateContract.as_view()),
    path('contracts/<int:pk>', ContractDetail.as_view()),
    path('events', ListCreateEvent.as_view()),
    path('events/<int:pk>', EventDetail.as_view()),
]
