# Generated by Django 4.0.6 on 2023-01-04 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_age_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=5, null=True),
        ),
    ]
