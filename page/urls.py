from django.urls import path
from .import views

urlpatterns = [
    path("", views.PageList.as_view(), name="Page-List")
]