from django.contrib import admin
from .models import Bb

class BbAdmin(admin.ModelAdmin):
  list_display = ('title', 'content', 'price', 'published')
  list_display_links = ('title', 'content')
  search_fields = ('title', 'content', 'price', 'published')

class RubricAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_display_links = ('name',)
  search_fields = ('name',)

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, RubricAdmin)

# Register your models here.
