# Generated by Django 2.1.1 on 2018-09-23 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meryota', '0004_auto_20180923_0510'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cat',
            new_name='Category',
        ),
    ]
