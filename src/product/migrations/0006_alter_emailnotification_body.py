# Generated by Django 5.0.4 on 2024-05-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_emailnotification_usernotification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailnotification',
            name='body',
            field=models.CharField(max_length=5000),
        ),
    ]
