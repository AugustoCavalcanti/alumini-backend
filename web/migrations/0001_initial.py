# Generated by Django 2.2.3 on 2019-08-15 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('ano', models.IntegerField(max_length=4)),
                ('semestre', models.IntegerField(max_length=1)),
                ('paraninfo', models.CharField(max_length=128)),
                ('patrono', models.CharField(max_length=128)),
                ('foto', models.URLField(blank=True, max_length=300, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turmas', to='web.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, unique=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habilidades', to='web.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Formando',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('ocupacao', models.CharField(max_length=128)),
                ('formacao', models.CharField(max_length=128)),
                ('foto', models.URLField(blank=True, max_length=300, null=True)),
                ('redes_socias', models.URLField(blank=True, null=True)),
                ('destaque', models.CharField(max_length=128)),
                ('local', models.CharField(max_length=128)),
                ('frase_de_efeito', models.CharField(max_length=300)),
                ('ano', models.IntegerField(max_length=4)),
                ('semestre', models.IntegerField(max_length=1)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='egressos', to='web.Curso')),
                ('habilidades', models.ManyToManyField(blank=True, max_length=5, related_name='egressos', to='web.Habilidade')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='egressos', to='web.Turma')),
            ],
        ),
    ]
