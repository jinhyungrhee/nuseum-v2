# Generated by Django 4.0.6 on 2022-10-14 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='NPP01',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP02',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP03',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP04',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP05',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP06',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP07',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP08',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP09',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP10',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP11',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP12',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP13',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP14',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP15',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP16',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP17',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP18',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP19',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='NPP20',
        ),
        migrations.AddField(
            model_name='notice',
            name='user_list',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
