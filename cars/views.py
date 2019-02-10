from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	#Complete Me
	form = CarForm()
	if request.method == "POST":
		form = CarForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('car-list')
		print (form.errors)
	context = {
	"form": form,
	}
	return render(request, 'create_car.html', context)


def car_update(request, car_id):
	#Complete Me
	car = Car.objects.get(id=car_id)
	form = CarForm(instance=car)
	if request.method == "POST":
		form = CarForm(request.POST, request.FILES or None, instance=car)
		if form.is_valid():
			form.save()
			return redirect('car-list')
		print (form.errors)
	context = {
	"form": form,
	"car": car,
	}
	return render(...)


def car_delete(request, car_id):
	#Complete Me
	Car.objects.get(id=car_id).delete()
	messages.success(request, "Successfully Deleted!")
	return redirect('car-list')
	return render(...)