# Generated by Django 3.2.9 on 2022-05-22 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_auto_20220522_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='dataEmprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 13, 25, 57, 38871), help_text='Informe a data de empréstimo do livro', verbose_name='Data do Empréstimo'),
        ),
    ]
