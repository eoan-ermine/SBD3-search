# Generated by Django 3.2 on 2022-07-27 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('second_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='First name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to='users.company')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='users.job')),
            ],
        ),
    ]
