from django.urls import path
from .views import PublicationList

urlpatterns = [
    path('', PublicationList.as_view(), name="publication_list"),
]