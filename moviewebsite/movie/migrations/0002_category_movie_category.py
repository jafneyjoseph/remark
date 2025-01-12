# Generated by Django 4.1 on 2024-03-17 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(default=-1986, on_delete=django.db.models.deletion.CASCADE, to='movie.category'),
            preserve_default=False,
        ),
    ]
