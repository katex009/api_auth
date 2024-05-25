from django.urls import path
from .views import PublicationList, PublicationDetail
urlpatterns = [
    path('', PublicationList.as_view(), name="publication_list"),
    path('<int:pk>/', PublicationDetail.as_view(), name="publication_detail"),
]