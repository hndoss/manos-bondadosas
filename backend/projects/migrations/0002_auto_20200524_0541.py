# Generated by Django 3.0.5 on 2020-05-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]