# Generated by Django 4.2.7 on 2024-02-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customertodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('mobileno', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
