# Generated by Django 3.0.5 on 2020-04-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitalinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ishospital',
            name='id',
        ),
        migrations.AlterField(
            model_name='hospitalinfo',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ishospital',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
