# Generated by Django 5.1.5 on 2025-01-31 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_blog', '0006_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_date']},
        ),
    ]
