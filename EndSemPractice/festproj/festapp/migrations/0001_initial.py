# Generated by Django 5.1.5 on 2025-04-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('rollno', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=20)),
                ('email', models.EmailField(max_length=128)),
                ('dept', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE')], max_length=128)),
            ],
        ),
    ]
