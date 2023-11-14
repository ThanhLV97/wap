from django.urls import path

from .views import (ActionDetailViewSet, ActionViewSet, DataIngestionDetail,
                    DataIngestionList, FilesViewSet, FileUploadView,
                    FileUploadViewSet, ModelDetailViewSet, ModelViewSet)

urlpatterns = [

    path('models/', ModelViewSet.as_view()),
    path('models/<int:pk>/', ModelDetailViewSet.as_view()),

    path('data/', DataIngestionList.as_view()),
    path('data/<int:pk>/', DataIngestionDetail.as_view()),

    path('actions/', ActionViewSet.as_view()),
    path('actions/<int:pk>/', ActionDetailViewSet.as_view()),

    path('upload/', FileUploadViewSet.as_view(), name='upload'),
    path('files/<str:filename>/', FilesViewSet.as_view(), name='files'),
    path('files/', FileUploadView.as_view(), name='files')

]
