# Generated by Django 4.1.5 on 2023-01-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_test_subject_alter_test_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
