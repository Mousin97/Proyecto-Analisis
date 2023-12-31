# Generated by Django 5.0 on 2023-12-14 20:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appmatricula', '0002_alter_matricula_matricula_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='Correo',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='La direccion de correo electronico no es valida')]),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Identidad',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='La identidad debe tener 13 digitos', regex='^[0-9]{13}$')]),
        ),
        migrations.AlterField(
            model_name='maestros',
            name='Correo',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='La direccion de correo electronico no es valida')]),
        ),
        migrations.AlterField(
            model_name='maestros',
            name='Identidad',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='La identidad debe tener 13 digitos', regex='^[0-9]{13}$')]),
        ),
        migrations.DeleteModel(
            name='Clase',
        ),
    ]
