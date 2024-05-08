# Generated by Django 4.1 on 2024-03-24 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0007_alter_movie_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(default=-1986, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]