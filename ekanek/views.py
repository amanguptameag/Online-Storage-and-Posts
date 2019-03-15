from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from myfile.models import UploadFile, Share


def home(request):
	if request.POST:
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=email, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
		    return redirect('register')

	mypic=[]
	lists = Share.objects.all()
	for obj in lists:
		a = UploadFile.objects.all().filter(user=obj.user, title=obj.title)
		for i in a:
			aa = []
			aa.append(i.user)
			aa.append(i.title)
			aa.append(i.file)
			mypic.append(aa)

	return render(request, 'home.html', {'mypic': mypic,})


def register(request):
	if request.POST:
		email = request.POST.get('email')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')

		if password==password2:
			user = User.objects.create_user(username=email, password=password)
			return redirect('home')
		else:
			return render(request, "register.html", {"s":"* password not matched"})

	return render(request, "register.html", {})

def log_out(request):
	logout(request)
	return redirect('home')
