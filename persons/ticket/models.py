from django.db import models


class Users(models.Model):
    name=models.CharField(max_length=25,verbose_name='enter your name')
    family=models.CharField(max_length=25,verbose_name='enter your family')
    phone=models.CharField(max_length=11,verbose_name='enter your phone number')
    def __str__(self):
        return self.name +'' ''+ self.family

class Ticket(models.Model):
    user=models.ForeignKey(Users, on_delete=models.CASCADE)
    Ticket_id=models.ForeignKey('self', on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=25,help_text='enter your title')
    description=models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    MONTHS_CHOICES = (('True','خوانده شده'),
                     ('False','خوانده نشده'))
    Condition = models.CharField(max_length=9,
                  choices=MONTHS_CHOICES,
                  default=False
                  )

    def __str__(self):
        return self.title 