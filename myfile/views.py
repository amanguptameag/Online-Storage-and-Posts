from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadForm
from .models import UploadFile, Share


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})


def view(request):
    if request.method == 'POST':
        delete = request.POST.get('delete')
        share = request.POST.get('share')
        if delete:
            UploadFile.objects.all().filter(user=request.user, title=delete).delete()
        if share:
            Share.objects.create(user=request.user, title=share)
            return redirect('home')
    list = UploadFile.objects.all().filter(user=request.user)
    return render(request, 'view.html', {'list': list})
