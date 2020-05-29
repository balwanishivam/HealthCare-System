# Generated by Django 3.0.4 on 2020-05-29 05:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='email')),
                ('user_type', models.CharField(choices=[('AMB', 'Ambulance'), ('BLB', 'Blood-Bank'), ('HSP', 'Hospital'), ('MST', 'Medical-Store')], max_length=3)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date-joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last-login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)])),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
