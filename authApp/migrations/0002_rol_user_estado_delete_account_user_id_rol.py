# Generated by Django 4.0.6 on 2023-05-19 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='estado',
            field=models.CharField(default='Activo', max_length=50, verbose_name='Estado'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='user',
            name='id_rol',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, related_name='id_rol', to='authApp.rol'),
        ),
    ]
