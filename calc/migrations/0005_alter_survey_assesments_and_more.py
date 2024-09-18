# Generated by Django 5.1 on 2024-08-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_rename_question_2_survey_assesments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='assesments',
            field=models.CharField(choices=[('written exams', 'written exams'), ('tests', 'tests'), ('puzzeles', 'puzzeles')], default='written exams', max_length=20),
        ),
        migrations.AlterField(
            model_name='survey',
            name='optimum_learning',
            field=models.CharField(choices=[('logical learning', 'logical learning'), ('creative learning', 'creative learning'), ('analitical learning', 'analitical learning')], default='logical learning', max_length=20),
        ),
    ]
