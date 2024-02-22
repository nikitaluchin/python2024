# Generated by Django 5.0 on 2024-02-21 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('house_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StaffType',
            fields=[
                ('staff_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('contact_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(max_length=1)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.address')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
                ('staff_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stafftype')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('room', models.IntegerField()),
                ('age', models.IntegerField()),
                ('diagnosis', models.CharField(max_length=100)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
                ('supervised_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
            ],
        ),
    ]