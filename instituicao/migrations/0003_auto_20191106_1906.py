# Generated by Django 2.2.7 on 2019-11-06 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0002_auto_20191106_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instituicao',
            old_name='password',
            new_name='senha',
        ),
    ]