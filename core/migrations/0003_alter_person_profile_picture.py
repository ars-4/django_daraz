# Generated by Django 4.0.4 on 2023-01-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_person_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
