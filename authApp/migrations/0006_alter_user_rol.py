# Generated by Django 4.0.6 on 2023-05-19 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0005_rename_id_rol_user_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id_rol', to='authApp.rol'),
        ),
    ]
