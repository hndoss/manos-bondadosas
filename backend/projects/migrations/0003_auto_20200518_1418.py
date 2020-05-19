# Generated by Django 3.0.5 on 2020-05-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200518_0557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectcategory',
            options={'verbose_name': 'Project Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='taskcategory',
            options={'verbose_name': 'Task Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='place',
            new_name='direction',
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
