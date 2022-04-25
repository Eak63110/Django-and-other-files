from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from .models import ContactMessage
from .models import TodoListItem

def Home(request):
	# return HttpResponse('<h1>Hello World</h1>')
	return render(request, 'home/home.html')

def Todolist(request):
	if request.method == 'POST':
		x = request.POST.copy()
		todolist = x.get('todolist')
		print(todolist)
		new_1 = TodoListItem()
		new_1.todolist = todolist
		new_1.save()
	all_todo_items = TodoListItem.objects.all()
	return render(request, 'home/service.html', {'all_items':all_todo_items})


def Contact(request):

	context = {}

	if request.method == 'POST':
		data = request.POST.copy()
		Email = data.get('email')
		inquiry = data.get('subject')
		content = data.get('detail')
		print(Email,content,inquiry)

		if Email == '' or content == '' :
			context['status'] = 'Alert '
			return render(request, 'home/contact.html',context)

		send_mail(
			subject=inquiry,
			message=content,
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[settings.RECIPIENT_ADDRESS]
		)

		new = ContactMessage()
		new.Email = Email
		new.inquiry = inquiry
		new.content = content
		new.save()
		
		context['status'] = 'success'

	return render(request, 'home/contact.html',context)





