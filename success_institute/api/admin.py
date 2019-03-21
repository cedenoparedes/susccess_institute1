from django.contrib import admin
from api import models
# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Group)
admin.site.register(models.student_group)
