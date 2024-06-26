# Generated by Django 5.0.6 on 2024-06-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام و نام خانوادکی')),
                ('email', models.EmailField(max_length=40, verbose_name='ایمیل')),
                ('phone', models.IntegerField(verbose_name='شماره تلفن')),
                ('number', models.PositiveIntegerField(verbose_name='تعداد')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاریخ')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='ساعت')),
            ],
            options={
                'verbose_name_plural': 'ثبت نام',
            },
        ),
    ]
