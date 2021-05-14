from django.contrib import admin
from .models import Blogpost
from .models import Mainblogpost
from .models import Message
# Register your models here.

admin.site.register(Blogpost)
admin.site.register(Mainblogpost)
admin.site.register(Message)