# Generated by Django 4.0.4 on 2022-05-19 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.IntegerField(null=True),
        ),
    ]
