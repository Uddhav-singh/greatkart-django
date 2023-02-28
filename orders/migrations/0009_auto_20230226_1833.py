# Generated by Django 3.1 on 2023-02-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20230215_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('New', 'New'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=10),
        ),
    ]
