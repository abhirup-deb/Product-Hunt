# Generated by Django 2.2 on 2019-04-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=40)),
                ('Pass', models.CharField(max_length=20)),
                ('ConfPass', models.CharField(max_length=20)),
            ],
        ),
    ]
