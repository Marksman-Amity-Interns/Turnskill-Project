# Generated by Django 3.2.4 on 2021-06-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210617_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isonetoone',
            field=models.BooleanField(default=False),
        ),
    ]
