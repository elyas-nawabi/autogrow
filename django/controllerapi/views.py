from msilib import schema
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
from .serializers import *
from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
import coreapi
from rest_framework.schemas import AutoSchema
# Create your views here.

class TaskListViewSchema(AutoSchema):
    def get_manual_fields(self,path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('desc')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields
            
        
class TaskList(APIView):
    """
    List all tasks, or create a new task.
    """
    
    schema = TaskListViewSchema()

    def get(self, request, format=None):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    """
    Retrieve, update or delete a task instance.
    """
    schema = TaskListViewSchema()

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# The bellow codes are the function based approach of views 

# @api_view(['GET', 'POST'])
# def commands_list(request):
#     """
#     List all code snippets, or create a new command.
#     """
#     if request.method == 'GET':
#         command = Command.objects.all()
#         serializer = CommandSerializer(command, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CommandSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def commands_detail(request, task_id):
#     """
#     Retrieve, update or delete commands.
#     """
#     #print(request.method," test 1")

#     try:
#         command = Command.objects.get(task_id=task_id)
#     except Command.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CommandSerializer(command)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CommandSerializer(command, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         # print(request.method," test 2")
#         command.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# this bellow code is just for developer test.
# def home(request):
#     return JsonResponse({'api':'controller api'})