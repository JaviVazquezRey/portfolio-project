# Generated by Django 2.2 on 2020-04-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200421_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='idUser',
            field=models.IntegerField(db_index=True, default=4, editable=False, primary_key=True, serialize=False),
        ),
    ]
