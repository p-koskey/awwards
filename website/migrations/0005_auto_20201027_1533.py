# Generated by Django 3.1.2 on 2020-10-27 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20201027_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='creativity',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='creativityaverage',
            new_name='contentaverage',
        ),
    ]
