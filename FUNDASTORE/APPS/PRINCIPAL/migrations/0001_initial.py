# Generated by Django 3.1.5 on 2021-02-12 19:04

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blg_id', models.AutoField(primary_key=True, serialize=False)),
                ('blg_tipo', models.CharField(choices=[('R', 'RECETAS'), ('N', 'NOTICIAS')], max_length=1)),
                ('blg_titulo', models.CharField(max_length=128)),
                ('blg_banner', models.ImageField(max_length=255, upload_to='blog/banners')),
                ('blg_video', models.URLField()),
                ('blg_post', tinymce.models.HTMLField()),
                ('blg_fecha_post', models.DateTimeField(auto_now_add=True)),
                ('blg_fecha_act', models.DateField(auto_now=True)),
            ],
        ),
    ]
