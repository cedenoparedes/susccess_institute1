# Generated by Django 2.1.7 on 2019-03-07 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_student_group_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
