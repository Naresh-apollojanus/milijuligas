# Generated by Django 3.1 on 2020-08-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gas_order', '0002_sms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('choose_cylinder', models.CharField(max_length=30, null=True)),
                ('qty', models.IntegerField()),
                ('time', models.CharField(max_length=30, null=True)),
                ('path_name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='sms',
            name='results',
            field=models.TextField(),
        ),
    ]
