# Generated by Django 3.2.8 on 2021-11-10 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20211111_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='qualifications',
        ),
        migrations.RemoveField(
            model_name='job',
            name='responsibility',
        ),
    ]
