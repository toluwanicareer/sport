# Generated by Django 2.1.1 on 2018-09-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180917_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='opp',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='team',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
