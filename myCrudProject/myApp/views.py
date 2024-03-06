from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializedData  = StudentSerializer(student)
            jsonData = JSONRenderer().render(serializedData.data)
            return HttpResponse(jsonData, content_type ='application/json')
        
    student = Student.objects.all()
    serializedData = StudentSerializer(student, many=True)
    jsonData = JSONRenderer().render(serializedData.data)
    return HttpResponse(jsonData, content_type='application/json')
