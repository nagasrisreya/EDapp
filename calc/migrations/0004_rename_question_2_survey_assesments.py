# Generated by Django 5.1 on 2024-08-30 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_rename_question_1_survey_optimum_learning'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='question_2',
            new_name='assesments',
        ),
    ]
