# Generated by Django 4.1.2 on 2022-11-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuariosAnfibio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=64)),
                ('apellido', models.CharField(default='', max_length=64)),
                ('email', models.CharField(default='', max_length=64)),
                ('nroCelular', models.CharField(default='', max_length=64)),
                ('contra', models.CharField(default='', max_length=64)),
                ('codigoUsr', models.CharField(default='OP-0000', max_length=64)),
            ],
        ),
    ]
