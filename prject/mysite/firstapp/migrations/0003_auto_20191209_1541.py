# Generated by Django 2.0.5 on 2019-12-09 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Album'),
        ),
    ]