# Generated by Django 3.2.9 on 2022-06-11 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0018_alter_emprestimo_dataemprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='dataPrazoDevolucao',
            field=models.DateField(blank=True, default=datetime.date(2022, 6, 17), help_text='Informe a data máxima de devolução do livro', null=True, verbose_name='Data Máxima de Devolução'),
        ),
        migrations.AddField(
            model_name='livro',
            name='quantidade',
            field=models.IntegerField(default=4, help_text='Informe a Quantidade de livros', verbose_name='Qtde.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataDevolucao',
            field=models.DateField(blank=True, help_text='Informe a data de devolução do livro', null=True, verbose_name='Data de Devolução'),
        ),
    ]