from django.urls import include,path
from controllerapi import views

urlpatterns = [
    path('',views.TaskList.as_view(), name="tasklist")
]
