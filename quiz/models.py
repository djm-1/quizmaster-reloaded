from django.db import models

#import uuid
# Create your models here.


class quiz(models.Model):
    
    contest_id=models.UUIDField(default=None)
    #question_id=models.AutoField
    question=models.TextField(max_length=300,default=None)
    option_1=models.CharField(max_length=100,default=None)
    option_2=models.CharField(max_length=100,default=None)
    option_3=models.CharField(max_length=100,default=None)
    option_4=models.CharField(max_length=100,default=None)
    answer=models.CharField(max_length=100,default=None)
    def __str__(self):
        return self.question

class leaderboard(models.Model):
    contest_id=models.UUIDField(default=None)
    participant_name=models.CharField(max_length=100,default=None)
    score=models.IntegerField(default=0)
    submit_time=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.participant_name