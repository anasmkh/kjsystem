from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,logout,authenticate
from mother.models import Mother,Child
from mother.childform import ChildForm, userCreation


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('mother')
    else:
        messages.error(request,'can not do this')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('mother')
        else:
            messages.error(request,'username or password is incorrect')

    return render(request,'login-register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = userCreation()

    if request.method == 'POST':
        form = userCreation(request.POST)
        if form.is_valid():
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request,user)
            return redirect('mother')
        else:
            messages.error(request,'Can\'t register')
    context = {'page':page,'form':form}
    return render(request,'login-register.html',context)

@login_required(login_url='login')
def profile(request,pk):
    child = Child.objects.get(id=pk)
    conext = {'child':child}
    return render(request,'profile.html',conext)

@login_required(login_url='login')
def mothers(request):
    mother = request.user.mother
    children = Child.objects.all()
    print(children)
    context = {'mother':mother,'children':children}
    return render(request,'mother.html',context)
@login_required(login_url='login')
def createChild(request,pk):
    mother = Mother.objects.get(id=pk)
    form = ChildForm()
    if request.method =='POST':
        form = ChildForm(request.POST,request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.mom = mother
            child.save()
            messages.success(request, 'This Child Created Successfully!')
            return redirect('/')
        else:
            form = ChildForm()
    context = {
        'form':form,
        'mother':mother
    }
    return render(request,'createchild.html',context)

def updateChild(request,pk):
    mother = request.user.mother
    child = mother.child_set.get(id=pk)
    form = ChildForm(instance=child)
    if request.method =='POST':
        form = ChildForm(request.POST,request.FILES,instance=child)
        if form.is_valid():
            child = form.save(commit=False)
            child.mom = mother
            child.save()
            messages.success(request, 'This Child Updated Successfully!')
            return redirect('mother')
        else:
            form = ChildForm()
    context = {
        'form':form,
        'mother':mother,
        'child':child
    }
    return render(request,'createchild.html',context)

def deleteChild(request,pk):
    mother = request.user.mother
    child = mother.child_set.get(id=pk)
    if request.method == 'POST':
        child.delete()
        return redirect('mother')
    context = {'object': child}
    return render(request, 'deleteform.html', context)

def choose_meals(request,pk):
    mother = request.user.mother
    child = mother.child_set.get(id=pk)
    form = ChildForm(instance=child)
    if request.method =='POST':
        form = ChildForm(request.POST,instance=child)
        if form.is_valid():
            child = form.save(commit=False)
            child.mom = mother
            child.save()
            messages.success(request, 'This Meal Choosen Successfully!')
            return redirect('mother')
        else:
            form = ChildForm()
    context = {
        'form':form,
        'mother':mother,
        'child': child
    }
    return render(request,'choose_meal.html',context)