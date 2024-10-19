# Generated by Django 3.1.3 on 2020-11-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=64)),
                ('key', models.CharField(max_length=256)),
                ('ban_time', models.PositiveIntegerField(default=21600)),
                ('api_name', models.CharField(max_length=512)),
                ('url_path', models.CharField(max_length=512)),
                ('rps', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
