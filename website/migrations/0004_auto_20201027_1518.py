# Generated by Django 3.1.2 on 2020-10-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20201027_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='creativity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='design',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='usability',
            field=models.IntegerField(null=True),
        ),
    ]
