# Generated by Django 3.0.4 on 2020-06-25 14:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('pincode', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)])),
                ('contact', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myuser.City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('distance_from_city_center', models.IntegerField()),
                ('pincode', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)])),
                ('contact', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myuser.City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine_Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mdf', models.DateField()),
                ('expiry', models.DateField()),
                ('mrp', models.PositiveIntegerField()),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medical_Store.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
