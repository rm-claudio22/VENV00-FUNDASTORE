# Generated by Django 3.1.5 on 2021-02-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTOS', '0007_auto_20210208_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='pro_imagen',
            field=models.ImageField(null=True, upload_to='C:\\Users\\Claudio Rivas\\OneDrive\\Escritorio\\FUNDADER\\Programacion II\\Python\\Django\\VENV00\\PROYECTOS\\FUNDASTORE\\FUNDASTORE/MEDIA\\PRODUCTOS'),
        ),
    ]
