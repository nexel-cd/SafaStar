# Generated by Django 5.0.1 on 2024-02-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0005_brandfaq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfaq',
            name='answer',
            field=models.TextField(verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='brandfaq',
            name='question',
            field=models.TextField(verbose_name='Question'),
        ),
    ]
