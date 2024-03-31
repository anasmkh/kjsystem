from django.shortcuts import render
from teacher.models import Teacher
from mother.models import Child, Mother
from mother.decorators import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from teacher.teacherForms import *

# @allowed_users(allowed_roles=['admin','teachers'])
def loginTeacher(request):
    if request.user.is_authenticated:
        return redirect('teachers')
    else:
        messages.error(request, 'can not do this')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('teachers')
        else:
            messages.error(request, 'username or password is incorrect')

    return render(request, 'log-reg.html')

@allowed_users(allowed_roles=['admin','teachers'])
def teacherRegisteration(request):
    page = 'register'
    form = TeacherCreation()
    if request.method == 'POST':
        form = TeacherCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('teachers')
        else:
            messages.error(request, 'Can\'t register')
    context = {'page': page, 'form': form}
    return render(request, 'log-reg.html', context)

@allowed_users(allowed_roles=['admin','teachers'])
def logoutUser(request):
    logout(request)
    return redirect('loginteacher')

@allowed_users(allowed_roles=['admin','teachers'])
def teachers(request):
    teachers = Teacher.objects.all()
    print(teachers)
    teacher = request.user.teacher
    children = Child.objects.all()
    context = {'children': children, 'teacher': teacher}
    return render(request, 'teachers.html', context)

@allowed_users(allowed_roles=['admin','teachers'])
def childprofile(request, pk):
    child = Child.objects.get(id=pk)
    context = {
        'child': child,
    }
    return render(request, 'childprofile.html', context)


def createReport(request,pk):
    teacher = request.user.teacher
    child = Child.objects.get(id=pk)
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
           report = form.save(commit=False)
           report.teacher = teacher
           report.child = child
           report.save()
           return redirect('teachers')
        else:
            ReportForm()
    context = {'teacher':teacher,'child':child,'form':form}
    return render(request,'reportform.html',context)

def readReport(request,pk):
    child = Child.objects.get(id=pk)
    report = child.report_set.all()
    context = {'child':child,'report':report}
    return render(request,'readreport.html',context)
