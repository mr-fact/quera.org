from email.policy import default

from django.db import models


class Problem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    score = models.PositiveIntegerField(default=100)
    writer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)



class Submission(models.Model):
    submitted_time = models.DateTimeField()
    code = models.URLField(max_length=200)
    score = models.PositiveIntegerField(default=0)
    participant = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='submissions')
    problem = models.ForeignKey('problems.Problem', on_delete=models.CASCADE, related_name='submissions')
