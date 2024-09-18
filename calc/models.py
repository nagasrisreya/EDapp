# models.py
from django.db import models

class Survey(models.Model):
    QUESTION_1_CHOICES = [
        ('logical learning', 'logical learning'),
        ('analitical learning', 'analitical learning'),
        ('creative learning', 'creative learning'),
    ]
    
    QUESTION_2_CHOICES = [
        ('written exams', 'written exams'),
        ('tests', 'tests'),
        ('puzzeles', 'puzzeles'),
    ]
    
    # QUESTION_3_CHOICES = [
    #     ('logical thinking', 'written exams'),
    #     ('', 'tests'),
    #     ('puzzeles', 'puzzeles'),
    # ]

    # QUESTION_4_CHOICES = [
    #     ('written exams', 'written exams'),
    #     ('tests', 'tests'),
    #     ('puzzeles', 'puzzeles'),
    # ]
    question_1 = models.CharField(max_length=20, choices=QUESTION_1_CHOICES, default='logical learning', name='optimum_learning')
    question_2 = models.CharField(max_length=20, choices=QUESTION_2_CHOICES, default='written exams', name='assesments')
