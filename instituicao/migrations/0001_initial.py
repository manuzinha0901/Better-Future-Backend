# Generated by Django 2.2.7 on 2019-11-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('responsavel', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('numero_casa', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
    ]
