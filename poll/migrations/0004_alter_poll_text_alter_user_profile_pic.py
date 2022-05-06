# Generated by Django 4.0 on 2022-04-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_alter_poll_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.FileField(upload_to='profile_pic/'),
        ),
    ]