# Generated by Django 5.1.1 on 2024-10-16 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blogmodel_usrproductmodel_productusermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productusermodel',
            old_name='up',
            new_name='up_name',
        ),
    ]
