# Generated by Django 4.2.7 on 2023-12-19 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='categeries',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.collections'),
        ),
    ]
