# Generated by Django 3.0.6 on 2020-06-05 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'Project Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, null=True)),
                ('description', models.CharField(max_length=120, null=True)),
                ('direction', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'Project Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('category', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'Task Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('due', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(max_length=60, null=True)),
                ('order', models.IntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.TaskCategory')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Collaborator')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCollaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collaborator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Collaborator')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectBeneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Beneficiary')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='beneficiaries',
            field=models.ManyToManyField(blank=True, related_name='projects', through='projects.ProjectBeneficiary', to='people.Beneficiary'),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projects.Category'),
        ),
        migrations.AddField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(blank=True, related_name='projects', through='projects.ProjectCollaborator', to='people.Collaborator'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projects.Status'),
        ),
    ]
