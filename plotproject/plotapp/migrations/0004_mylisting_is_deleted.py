# Generated by Django 4.2.5 on 2023-09-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotapp', '0003_rename_contactus_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylisting',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
