from rest_framework.response import Response
from rest_framework.decorators import api_view
from mother.models import Mother , Child
from teacher.models import Teacher
from API.serializers import *

@api_view(['GET'])
def getMoms(request):
    mothers = Mother.objects.all()
    serializer = MotherSerializer(mothers,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addMom(request):
    serializer = MotherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def childProfile(request):
    child = Child.objects.all()
    print(child)
    serialzer = ChildSerializer(child,many=True)
    return Response(serialzer.data)


@api_view(['GET'])
def getchild(request,pk):
    child = Child.objects.get(id=pk)
    print(child)
    serialzer = ChildSerializer(child,many=False)
    return Response(serialzer.data)

@api_view(['POST'])
def addChild(request):
    serializer = ChildSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateChild(request,pk):
    child = Child.objects.get(id=pk)
    serializer = ChildSerializer(instance=child,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['GET'])
def getTeacher(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers,many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteChild(request,pk):
    child = Child.objects.get(id=pk)
    child.delete()
    return Response('This Child has been deleted')

@api_view(['GET'])
def readReport(request,pk):
    child = Child.objects.get(id=pk)
    report = child.report_set.all()
    print(child)
    serializer = ReportSerializer(report,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createReport(request):
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

