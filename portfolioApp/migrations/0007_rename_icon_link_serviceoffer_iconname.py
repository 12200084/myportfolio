# Generated by Django 4.1.4 on 2023-02-16 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0006_serviceoffer_alter_copyright_copyright_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceoffer',
            old_name='icon_link',
            new_name='iconname',
        ),
    ]
