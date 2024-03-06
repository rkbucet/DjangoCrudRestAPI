from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        jsonData = request.body
        stream = io.BytesIO(jsonData)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)
        if id is not None:
            studentObjs = Student.objects.get(id=id)
            serializedData  = StudentSerializer(studentObjs)
            jsonData = JSONRenderer().render(serializedData.data)
            return HttpResponse(jsonData, content_type ='application/json')
        
        studentObjs = Student.objects.all()
        serializedData = StudentSerializer(studentObjs, many=True)
        jsonData = JSONRenderer().render(serializedData.data)
        return HttpResponse(jsonData, content_type='application/json')


    if request.method == 'POST':
        jsonData = request.body
        stream = io.BytesIO(jsonData)
        pythonData = JSONParser().parse(stream)
        serializedData = StudentSerializer(data = pythonData)
        if serializedData.is_valid():
            serializedData.save()
            response = {'message': 'Data Saved!'}
            jsonData = JSONRenderer().render(response)
            return HttpResponse(jsonData, content_type='application/json')
        jsonData = JSONRenderer().render(serializedData.errors)
        return HttpResponse(jsonData, content_type='application/json')
    

    if request.method == 'PUT':
        jsonData = request.body
        stream = io.BytesIO(jsonData)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        studentObjs = Student.objects.get(id = id)
        serializedData = StudentSerializer(studentObjs, data=pythonData, partial=True)
        if serializedData.is_valid():
            serializedData.save()
            response = {'message':'Data Updated!'}
            jsonData = JSONRenderer().render(response)
            return HttpResponse(jsonData, content_type='application/json')
        jsonData = JSONRenderer().render(serializedData.errors)
        return HttpResponse(jsonData, content_type='application/json')


