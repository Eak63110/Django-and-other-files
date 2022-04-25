from django.conf import settings
from django.core.mail import send_mail
from django.db import models

class ContactMessage(models.Model):
	Email = models.EmailField(max_length = 254)
	content = models.TextField(blank=True, null=True)
	inquiry = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.Email


class TodoListItem(models.Model):
    todolist = models.TextField(blank=True, null=True)

    def __str__(self):
    	return self.todolist