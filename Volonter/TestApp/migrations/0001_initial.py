# Generated by Django 3.1.3 on 2020-11-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.TextField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('src', models.TextField()),
            ],
        ),
    ]