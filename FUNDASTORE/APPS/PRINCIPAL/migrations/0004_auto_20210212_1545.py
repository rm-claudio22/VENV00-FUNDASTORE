# Generated by Django 3.1.5 on 2021-02-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRINCIPAL', '0003_blog_blg_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blg_fecha_act',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
