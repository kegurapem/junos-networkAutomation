# Generated by Django 4.2.4 on 2023-09-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioNornir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('administrador', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'usuarionornir',
            },
        ),
    ]