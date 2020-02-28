# Generated by Django 3.0.2 on 2020-02-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200203_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('zip_code', models.IntegerField(default=0)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
    ]