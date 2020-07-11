# Generated by Django 3.0.7 on 2020-07-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField(verbose_name='text')),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
