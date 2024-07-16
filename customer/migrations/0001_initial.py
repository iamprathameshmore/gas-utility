# Generated by Django 5.0.6 on 2024-07-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GasRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('req_id', models.CharField(blank=True, max_length=50, null=True)),
                ('discription', models.CharField(blank=True, max_length=5000, null=True)),
                ('current_state', models.CharField(default='incomplete', max_length=100)),
                ('submit_at', models.DateTimeField(auto_now=True)),
                ('resolve_at', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('otp_secret', models.CharField(blank=True, max_length=16, null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]
