from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import ToDo

# Create your views here.
def index(request):
	todo_list = ToDo.objects.all().order_by('-date')
	return render(request, 'main/index.html', {
		'todos': todo_list
	})

def add_todo(request):
	# catch post data and date
	text = request.POST.get('text')
	date = timezone.now()
	# save into database
	ToDo.objects.create(date=date, text=text)
	return HttpResponseRedirect(reverse('index'))

def delete_todo(request, todo_id):
	ToDo.objects.get(id=todo_id).delete()
	return HttpResponseRedirect(reverse('index'))