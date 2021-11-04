from django.urls import path, include
from django.conf.urls import url
from .views import ClientDetail

urlpatterns = [
    path('clients/<int:pk>', ClientDetail.as_view()),

]
