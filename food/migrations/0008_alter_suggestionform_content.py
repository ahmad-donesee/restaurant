# Generated by Django 5.0.6 on 2024-05-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_suggestionform_alter_categoryfood_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestionform',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]