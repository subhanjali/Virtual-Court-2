# Generated by Django 3.1.7 on 2021-04-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0012_auto_20210424_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to='cases'),
        ),
    ]
