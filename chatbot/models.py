from django.db import models
from django.contrib.auth.models import User

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question

class ClientQuestion(models.Model):
    question = models.CharField(max_length=255)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_assigned = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_questions', blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.question
