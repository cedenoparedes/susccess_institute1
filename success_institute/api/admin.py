from django.contrib import admin
from api import models
# Register your models here.

admin.site.register(models.student)
admin.site.register(models.group)
admin.site.register(models.student_group)
