# Generated by Django 2.0.1 on 2018-01-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=140)),
                ('date_time', models.DateField(verbose_name='保存日')),
            ],
        ),
    ]