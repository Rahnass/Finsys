# Generated by Django 4.1 on 2022-09-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_itemtable_account_sal_itemtable_acount_pur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtable',
            name='status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
