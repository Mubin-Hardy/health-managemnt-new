# Generated by Django 4.0.5 on 2022-06-26 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('by', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
