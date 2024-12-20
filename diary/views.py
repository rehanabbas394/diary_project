from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DiaryEntry
from .serializers import DiaryEntrySerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DiaryEntryForm 
from django.contrib.auth import logout

//Make something good project. Crud API is for freshers like e-commerce and handles media and payment methods. 

@api_view(['GET', 'POST'])
def diary_list(request):
    if request.method == 'GET':
        entries = DiaryEntry.objects.filter(user=request.user)
        serializer = DiaryEntrySerializer(entries, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DiaryEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def diary_detail(request, pk):
    try:
        entry = DiaryEntry.objects.get(pk=pk, user=request.user)
    except DiaryEntry.DoesNotExist:
        return Response({'error': 'Entry not found or not yours'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiaryEntrySerializer(entry)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DiaryEntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        entry.delete()
        return Response({'message': 'Entry deleted'}, status=status.HTTP_204_NO_CONTENT)



//Remove extra spaces it seems like copying from AI tools


# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            return HttpResponse("Invalid credentials", status=400)
    return render(request, 'login.html')



# Register View
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard') 
    return render(request, 'register.html')

// use class base 


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login.html')  




# Dashboard View
@login_required
def dashboard_view(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'entries': entries})




# Add Entry View
@login_required
def add_entry_view(request):
    if request.method == "POST":
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('dashboard')
    else:
        form = DiaryEntryForm()
    return render(request, 'add_entry.html', {'form': form})



# Edit Entry View
@login_required
def edit_entry_view(request, id):
    entry = DiaryEntry.objects.get(id=id, user=request.user)
    if request.method == "POST":
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'edit_entry.html', {'form': form})



# Delete Entry View
@login_required
def delete_entry_view(request, id):
    entry = DiaryEntry.objects.get(id=id, user=request.user)
    entry.delete()
    return redirect('dashboard')



