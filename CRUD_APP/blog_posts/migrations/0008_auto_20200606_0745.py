# Generated by Django 3.0.6 on 2020-06-06 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0007_auto_20200606_0738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]
