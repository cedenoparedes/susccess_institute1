from django.contrib.auth.models import User, AbstractUser
from django.db import models

class student(models.Model):

    user = models.ForeignKey(User, related_name='user_student_id', on_delete=models.DO_NOTHING)
    career = models.CharField( max_length=128, blank=True, null=True)


class group(models.Model):
    name = models.CharField( max_length=128, blank=True, null=True)


class student_group(models.Model):
    student = models.ForeignKey(student,related_name ='student_group_id', on_delete=models.DO_NOTHING)
    group_id = models.ForeignKey(group, related_name='student_group_id', on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)


class teacher(models.Model):
    user = models.ForeignKey(User, related_name='teacher_user_id', on_delete=models.DO_NOTHING)
    specialty = models.CharField(max_length=100, blank=True, null=False)


class location(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    adreess = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)


class classroom(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    location_id = models.ForeignKey(location, related_name='classroom_location_id', on_delete=models.DO_NOTHING)


class subject(models.Model):
    name = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=True)


class homework(models.Model):
    file = models.FileField(blank=True, upload_to='license')
    image = models.ImageField()
    description = models.CharField(max_length=200, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    close_at = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True, blank=True)


class class_details(models.Model):
    student_group_id = models.ForeignKey(student_group, related_name='student_group_id', on_delete=models.DO_NOTHING)
    teacher_id = models.ForeignKey(teacher, related_name='teacher_class_id', on_delete=models.DO_NOTHING)
    classroom_id = models.ForeignKey(classroom, related_name='classroom_class_id', on_delete=models.DO_NOTHING)
    subject_id = models.ForeignKey(subject, related_name='class_subject_id', on_delete=models.DO_NOTHING)
    homework_id = models.ForeignKey(homework,related_name='class_homework_id', on_delete=models.DO_NOTHING, blank=True)
    start_at = models.DateTimeField(auto_now_add=True, blank=True)
    finish_at = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True, blank=True)
