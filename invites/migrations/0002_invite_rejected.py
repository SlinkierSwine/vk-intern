# Generated by Django 4.2.1 on 2023-05-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
