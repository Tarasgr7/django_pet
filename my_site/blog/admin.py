from django.contrib import admin
from .models import Post,Author,Tag, Comments
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter=("author","date","tag")
    list_display=("title","author","date")
    prepopulated_fields={"slug":("title",)}
admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comments)