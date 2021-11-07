from django.urls import path, include
from django.conf.urls import url
from .views import ClientDetail, CreateClient

urlpatterns = [
    path('clients/<int:pk>', ClientDetail.as_view()),
    path('clients', CreateClient.as_view()),
]
