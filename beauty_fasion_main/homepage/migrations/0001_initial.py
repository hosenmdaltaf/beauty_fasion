# Generated by Django 3.0 on 2021-12-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery_img')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='review_img')),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='team_img')),
                ('Specialist', models.CharField(blank=True, max_length=80, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]