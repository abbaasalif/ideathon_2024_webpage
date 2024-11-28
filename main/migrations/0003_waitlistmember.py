# Generated by Django 4.2.16 on 2024-10-16 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_registeredmember_team_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaitlistMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('panther_id', models.IntegerField(unique=True)),
                ('degree', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=50)),
                ('csc_1302', models.BooleanField()),
            ],
        ),
    ]
