# Generated by Django 4.1 on 2022-09-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_itemtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtable',
            name='inventry',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemtable',
            name='stock',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
