# Generated by Django 3.2.6 on 2021-08-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_subject_subjectname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subjectName',
            field=models.CharField(max_length=30),
        ),
    ]
