# Generated by Django 3.0.8 on 2020-09-03 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news_add_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
    ]