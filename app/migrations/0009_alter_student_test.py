# Generated by Django 4.1.5 on 2023-01-08 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_student_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='app.test'),
        ),
    ]