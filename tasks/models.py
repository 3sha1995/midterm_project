from django.db import models
from datetime import date

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100) #required 
    description = models.TextField(blank=True, null=True)# optional 
    due_date = models.DateField() #required 
    
    def status(self):
        today = date.today()

        if self.due_date < today:
            status = "Overdue"
        elif self.due_date == today:
            status = "Due Today"
        else:
            status = "Upcoming"

        return f"{status}"
