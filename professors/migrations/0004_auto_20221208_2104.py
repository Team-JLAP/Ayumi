# Generated by Django 2.2 on 2022-12-09 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0003_auto_20221208_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professors.Profile'),
        ),
    ]