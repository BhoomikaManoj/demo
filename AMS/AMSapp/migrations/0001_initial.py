# Generated by Django 3.2.8 on 2021-10-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=100)),
                ('emailId', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=12)),
            ],
        ),
    ]