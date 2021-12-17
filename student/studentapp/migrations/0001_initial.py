# Generated by Django 4.0 on 2021-12-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('currentjob', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'studentinfo',
            },
        ),
    ]