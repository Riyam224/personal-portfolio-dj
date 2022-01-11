from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.


from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'image']


admin.site.register(Post , PostAdmin)