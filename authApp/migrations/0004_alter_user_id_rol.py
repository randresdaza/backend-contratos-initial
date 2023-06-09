# Generated by Django 4.0.6 on 2023-05-19 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_dependencia_serie_subserie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='id_rol', to='authApp.rol'),
        ),
    ]
