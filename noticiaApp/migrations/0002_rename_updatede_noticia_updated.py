# Generated by Django 4.0.4 on 2022-05-01 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticiaApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='updatede',
            new_name='updated',
        ),
    ]
