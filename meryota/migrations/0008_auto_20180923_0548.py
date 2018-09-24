# Generated by Django 2.1.1 on 2018-09-23 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meryota', '0007_auto_20180923_0519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meryota.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meryota.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='meryota.Membership', to='meryota.Person'),
        ),
    ]
