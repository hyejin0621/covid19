# Generated by Django 3.2.5 on 2022-03-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coviddig', '0002_covidper'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyCovid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('da_co', models.CharField(max_length=50)),
            ],
        ),
    ]