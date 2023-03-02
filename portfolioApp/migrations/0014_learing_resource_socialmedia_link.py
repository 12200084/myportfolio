# Generated by Django 4.1.7 on 2023-03-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0013_rename_mobile_application_projectcount_countdown_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='learing_resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_link', models.CharField(max_length=5000)),
                ('title', models.CharField(max_length=500)),
                ('resource_link', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='socialmedia_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_link', models.CharField(max_length=1000)),
                ('linked_link', models.CharField(max_length=1000)),
                ('facebook_link', models.CharField(max_length=1000)),
            ],
        ),
    ]
