# Generated by Django 2.0.1 on 2018-01-09 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('formato', models.CharField(max_length=20)),
                ('duracion', models.TimeField()),
                ('file', models.FileField(upload_to='')),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Categoria')),
            ],
        ),
    ]
