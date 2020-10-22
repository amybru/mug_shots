# Generated by Django 3.1.1 on 2020-10-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=222, max_length=200),
            preserve_default=False,
        ),
    ]
