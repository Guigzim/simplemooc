from django.contrib import admin

# Register your models here.
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','slug','start_date','created_at']
    search_fields = ['name','slug']
    prepopulated_fields = {'slug':['name']}
    

admin.site.register(Course, CourseAdmin)
title = 'Administrador de Cursos'
admin.site.site_title = title
admin.site.site_header = title