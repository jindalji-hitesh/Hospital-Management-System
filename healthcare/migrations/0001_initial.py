# Generated by Django 2.2.5 on 2019-11-22 18:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=100)),
                ('success', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(default='123456789', max_length=100)),
                ('email', models.CharField(default='hospital_email@gmail.com', max_length=100)),
                ('amount', models.PositiveIntegerField(default=100)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_time', models.DateTimeField(default=datetime.datetime.now)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField(blank=True, null=True)),
                ('prescription', models.TextField(default='Prescription will be filled by the doctor.')),
                ('status', models.CharField(choices=[('Unconfirmed', 'Unconfirmed'), ('Confirmed', 'Confirmed')], default='Confirmed', max_length=20)),
                ('fee', models.PositiveIntegerField(default=500)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.DoctorProfile')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.Transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
