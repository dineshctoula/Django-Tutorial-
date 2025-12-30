from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField()
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    # auto_now_add bhaneko chae data create huney bitikae automamtically time auxa ane teslae change garna mildaena





    def __str__(self):
        return self.title