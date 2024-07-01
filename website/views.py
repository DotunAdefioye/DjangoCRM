from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

    #check to see if logging in
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome to your account")
            return redirect('home')
        else:
            messages.success(request, "Invalid Username and/or Password, Please Try Again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})



def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)


            login(request, user)
            messages.success(request, f'Welcome {user}, you have successfully logged in')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #lookup record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, f'You must be logged in to view this page')
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, f'Record has been deleted successfully')
        return redirect('home')
    else:
        messages.success(request, f'You must be logged in to delete this record')
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid():
                add_record = form.save()

                messages.success(request, f'Record has been added successfully')
                return redirect('home')
        return render(request, 'add_record.html', {"form": form})
    else:
        messages.success(request, f'You must be logged in to add new record')
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=customer_record)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record has been updated successfully')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, f'You must be logged in to update record')
        return redirect('home')








