# Generated by Django 5.1.5 on 2025-02-04 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_blog', '0007_alter_comment_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='author',
            new_name='artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='song',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='song',
            name='songwriter',
        ),
    ]
