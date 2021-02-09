# Generated by Django 3.1.6 on 2021-02-09 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hash', models.CharField(max_length=255)),
                ('Height', models.IntegerField()),
                ('Timestamp', models.IntegerField()),
                ('Transactions', models.IntegerField()),
                ('Miner', models.CharField(max_length=255)),
            ],
        ),
    ]
