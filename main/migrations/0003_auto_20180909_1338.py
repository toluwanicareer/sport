# Generated by Django 2.1.1 on 2018-09-09 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180908_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='result',
            field=models.TextField(null=True),
        ),
    ]
