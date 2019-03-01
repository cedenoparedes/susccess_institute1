from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

class student(models.Model):
    user = models.ForeignKey(User, related_name='user_studente_id', on_delete=models.DO_NOTHING)



