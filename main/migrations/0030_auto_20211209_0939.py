# Generated by Django 3.2.9 on 2021-12-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_userstore_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstore',
            name='address',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='userstore',
            name='meli',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]