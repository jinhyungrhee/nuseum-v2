# Generated by Django 4.0.6 on 2022-10-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
