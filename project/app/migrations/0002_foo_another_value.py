# Generated by Django 2.2.6 on 2019-10-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foo',
            name='another_value',
            field=models.CharField(default='some_value', max_length=40),
            preserve_default=False,
        ),
    ]