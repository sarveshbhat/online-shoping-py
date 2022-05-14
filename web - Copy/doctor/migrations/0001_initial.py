# Generated by Django 3.2.4 on 2021-09-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('lic', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=100)),
                ('clinic', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
    ]
