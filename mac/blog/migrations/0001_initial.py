# Generated by Django 3.0.2 on 2020-02-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=50)),
                ('head10', models.CharField(default='', max_length=500)),
                ('chead10', models.CharField(default='', max_length=5000)),
                ('head11', models.CharField(default='', max_length=500)),
                ('chead11', models.CharField(default='', max_length=5000)),
                ('head12', models.CharField(default='', max_length=500)),
                ('chead12', models.CharField(default='', max_length=5000)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]