# Generated by Django 2.2.7 on 2019-11-06 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='confirmar_senha',
        ),
    ]
