# Generated by Django 5.0.6 on 2024-06-10 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(auto_now=True, null=True, verbose_name='تاریخ انتشار'),
        ),
    ]