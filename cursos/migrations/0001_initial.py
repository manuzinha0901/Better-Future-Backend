# Generated by Django 2.2.7 on 2019-11-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=255)),
                ('carga_horaria', models.CharField(max_length=255)),
                ('vagas_disponiveis', models.CharField(max_length=255)),
                ('horarios', models.CharField(max_length=255)),
            ],
        ),
    ]
