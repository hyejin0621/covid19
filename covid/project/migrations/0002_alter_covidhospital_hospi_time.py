# Generated by Django 3.2.5 on 2022-03-03 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidhospital',
            name='hospi_time',
            field=models.CharField(max_length=100),
        ),
    ]