# Generated by Django 5.1.3 on 2024-11-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0003_alter_blog_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='section',
            field=models.CharField(choices=[('Trending', 'Trending'), ('Popular', 'Popular'), ('Recent', 'Recent')], max_length=100),
        ),
    ]
