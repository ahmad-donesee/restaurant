# Generated by Django 4.2.7 on 2023-11-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='عکسها'),
        ),
    ]
