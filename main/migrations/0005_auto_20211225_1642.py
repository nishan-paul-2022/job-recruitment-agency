# Generated by Django 3.2.6 on 2021-12-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211225_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models_freelancer',
            name='emailaddress',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='models_freelancer',
            name='password',
            field=models.TextField(),
        ),
    ]
