# Generated by Django 2.2 on 2020-04-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('idUser', models.IntegerField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('descriptionShort', models.CharField(max_length=250)),
                ('descriptionLong', models.TextField()),
                ('dateCreation', models.DateTimeField()),
                ('imageProfile', models.ImageField(upload_to='images/')),
                ('isAdmin', models.BooleanField()),
            ],
        ),
    ]
