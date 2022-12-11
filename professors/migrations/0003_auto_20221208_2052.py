# Generated by Django 2.2 on 2022-12-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0002_auto_20221208_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='semester',
            field=models.CharField(max_length=30),
        ),
    ]
