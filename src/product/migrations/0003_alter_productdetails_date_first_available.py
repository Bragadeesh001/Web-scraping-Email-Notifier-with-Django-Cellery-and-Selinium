# Generated by Django 5.0.4 on 2024-04-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_userdetail_url_alter_userdetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='date_first_available',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
