# Generated by Django 5.0.3 on 2024-06-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_file_folder_alter_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]