# Generated by Django 2.2.12 on 2020-05-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0003_auto_20200520_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childrecord',
            name='behaviour',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childrecord',
            name='feeding',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childrecord',
            name='medication',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childrecord',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childrecord',
            name='visit',
            field=models.TextField(blank=True, null=True),
        ),
    ]