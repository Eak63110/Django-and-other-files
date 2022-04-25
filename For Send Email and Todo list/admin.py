from django.contrib import admin
from .models import ContactMessage
from .models import TodoListItem

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(TodoListItem)
