# Generated by Django 3.2.4 on 2021-06-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phoneNo', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
