# Generated by Django 3.1.2 on 2020-10-27 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20201027_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='contentaverage',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='designaverage',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='usabilityaverage',
        ),
    ]