from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class student(models.Model):
    user = models.ForeignKey(User, related_name='user_studente_id', on_delete=models.DO_NOTHING)
    career = models.CharField( max_length=128, blank=True, null=True)


class group(models.Model):
    name = models.CharField( max_length=128, blank=True, null=True)



class student_group(models.Model):
    student = models.ForeignKey(student,related_name ='student_group_id', on_delete=models.DO_NOTHING)
    group_id = models.ForeignKey(group, related_name='student_group_id', on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)




