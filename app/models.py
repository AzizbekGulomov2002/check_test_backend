from django.db import models
from datetime import datetime
# Create your models here.
class BotUser(models.Model):
    t_id = models.CharField(max_length=25,verbose_name="Telegram ID",unique=True)
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name="Name")
    surname = models.CharField(max_length=100,null=True,blank=True,verbose_name="Surname")
    language = models.CharField(max_length=5,default='uz',verbose_name="Language")
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.t_id
    @property
    def date(self):
        mydate = self.created
        time = mydate.strftime("%m/%d/%Y, %H:%M")
        return time
    
class Test(models.Model):
    user = models.ForeignKey(BotUser,on_delete=models.SET_NULL,to_field='t_id',related_name='tester',null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    code = models.CharField(max_length=100,null=True,blank=True,unique=True)
    answers = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super(Test, self).save(*args, **kwargs)
        if not self.code:
            self.code = 1000+self.id
        super(Test, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.code} raqamli test"
    @property
    def creator(self):
        return 'user'
            
       
    @property
    def date(self):
        mydate = self.created
        time = mydate.strftime("%m/%d/%Y, %H:%M")
        return time
class Student(models.Model):
    user = models.ForeignKey(BotUser,on_delete=models.CASCADE,to_field='t_id',related_name='student')
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='test',to_field='code')
    result = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f"{self.user.name}ning natijasi"
    @property
    def username(self):
        return self.user.name+' '+self.user.surname
    