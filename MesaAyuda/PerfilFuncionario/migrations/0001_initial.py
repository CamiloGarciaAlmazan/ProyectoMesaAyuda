# Generated by Django 3.1.2 on 2020-10-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='resuma su problema', max_length=200)),
                ('description', models.TextField(help_text='explique a detalle su problema', max_length=1000)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
