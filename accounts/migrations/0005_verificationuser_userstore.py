<<<<<<< Updated upstream
# Generated by Django 3.2.9 on 2021-11-22 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_alter_verificationuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationuser',
            name='userstore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
=======
# Generated by Django 3.2.9 on 2021-11-22 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_alter_verificationuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationuser',
            name='userstore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
>>>>>>> Stashed changes
