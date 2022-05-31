# Generated by Django 4.0.4 on 2022-05-01 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=500)),
                ('imagen', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updatede', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'noticia',
                'verbose_name_plural': 'noticias',
            },
        ),
    ]
