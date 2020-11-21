# Generated by Django 3.1.3 on 2020-11-20 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('college', '0003_auto_20201120_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercollege',
            name='user',
            field=models.OneToOneField(default=10, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]