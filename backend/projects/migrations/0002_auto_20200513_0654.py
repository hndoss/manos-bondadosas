# Generated by Django 3.0.5 on 2020-05-13 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborators', '0002_remove_collaborator_projects'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(blank=True, to='collaborators.Collaborator'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
