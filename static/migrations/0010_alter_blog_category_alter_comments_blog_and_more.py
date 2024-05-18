# Generated by Django 4.2.7 on 2023-11-29 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comments_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Blog', to='blog.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='blog.blog', verbose_name='نطرات'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='تاریخ انتشار'),
        ),
    ]
