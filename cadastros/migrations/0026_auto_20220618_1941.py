# Generated by Django 3.2.9 on 2022-06-18 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0025_alter_emprestimo_dataprazodevolucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(help_text='Selecione o livro a emprestar', null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadastros.livro'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='livro',
            field=models.ForeignKey(help_text='Selecione o livro a reservar', null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadastros.livro'),
        ),
    ]