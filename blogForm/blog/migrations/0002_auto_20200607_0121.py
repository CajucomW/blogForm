# Generated by Django 3.0.7 on 2020-06-07 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='username',
            field=models.CharField(max_length=127),
        ),
    ]