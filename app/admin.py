from django.contrib import admin

# Register your models here.
from .models import Comment, Path, Image

admin.site.register(Path)
admin.site.register(Comment)
admin.site.register(Image)