# Generated by Django 3.1.6 on 2021-02-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210217_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True),
        ),
    ]
