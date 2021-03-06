# Generated by Django 2.0.1 on 2018-01-30 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_video_caratula'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='fecha_estreno',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='sinopsis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='tipo_video_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.TipoVideo'),
        ),
    ]
