# Generated by Django 2.2.3 on 2019-09-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190916_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='overview',
            field=models.TextField(default='This is overviewfield plsese add your minimum overview'),
        ),
    ]
