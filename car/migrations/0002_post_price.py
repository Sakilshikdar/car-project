# Generated by Django 4.2.7 on 2023-12-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]