# Generated by Django 3.1.7 on 2021-03-28 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210328_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('gov', 'Government Jobs'), ('Free', 'fee courses online'), ('gov exam', 'government exams'), ('exam result', 'government exams result'), ('entrance exam', 'Entrance exam'), ('job notification', 'Job Notification'), ('internship', 'Internship'), ('work-form-home', 'work form home')], default='', max_length=50),
        ),
    ]
