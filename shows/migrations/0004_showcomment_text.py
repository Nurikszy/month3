# Generated by Django 4.0.1 on 2022-01-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_showcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='showcomment',
            name='text',
            field=models.TextField(null=True),
        ),
    ]