# Generated by Django 4.2.5 on 2023-09-23 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_password', models.CharField(max_length=100)),
                ('new_password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
            ],
        ),
    ]
