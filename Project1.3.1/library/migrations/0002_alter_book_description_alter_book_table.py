# Generated by Django 4.2.11 on 2024-04-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterModelTable(
            name='book',
            table=None,
        ),
    ]