from django.urls import path

from .views import (ActionDetailViewSet, ActionViewSet, DataIngestionDetail,
                    DataIngestionList, ModelDetailViewSet, ModelViewSet)

urlpatterns = [

    path('models/', ModelViewSet.as_view()),
    path('models/<int:pk>/', ModelDetailViewSet.as_view()),

    path('data/', DataIngestionList.as_view()),
    path('data/<int:pk>/', DataIngestionDetail.as_view()),

    path('actions/', ActionViewSet.as_view()),
    path('actions/<int:pk>/', ActionDetailViewSet.as_view()),

]