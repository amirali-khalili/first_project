from django.db import models

class manager(models.Model): #مدیر مدرسه
    manager_name = models.CharField(max_length=100,blank=False,null=False)
    family =models.CharField(max_length=25,verbose_name= 'family',blank=True,null=True)
    phone=models.CharField(max_length=11,verbose_name='  phone ',blank=True,null=True)
    def __str__(self):
        return F"{self.manager_name} {self.family}"

class schools(models.Model): #فیلد اصلی مدرسه
    name = models.CharField(max_length=100,blank=False,null=False)
    addres=models.CharField(max_length=50,verbose_name= 'enter your schools addres',blank=True,null=True)
    manager = models.OneToOneField(manager, on_delete=models.CASCADE)
    class_Lesson=models.ManyToManyField('class_Lesson',blank=True)
    def __str__(self):
        return self.name

class Moderator(models.Model):#ناظم مدرسه
    name = models.CharField(max_length=100,blank=True,null=True)
    family =models.CharField(max_length=25,verbose_name= 'enter your family',blank=False,null=False)
    phone=models.CharField(max_length=11,verbose_name='enter your phone number',blank=True,null=True)
    schools = models.ForeignKey(schools,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return F"{self.name} {self.family}"
    
    
class book(models.Model):#کتاب های مدرسه
    title = models.CharField(max_length=100,verbose_name='enter your title')
    book_sheet=models.IntegerField(verbose_name= 'enter your book_sheet',blank=True,null=True)
    def __str__(self):
            return self.title
    


class student(models.Model):# دانش آموزان مدرسه
    name =models.CharField(max_length=25,verbose_name= 'enter your name',blank=False,null=False)
    family =models.CharField(max_length=25,verbose_name= 'enter your family',blank=True,null=True)
    age=models.IntegerField(verbose_name= 'enter your age',blank=True,null=True)
    phone=models.CharField(max_length=11,verbose_name='enter your phone number',blank=True,null=True)
    books = models.ManyToManyField(book,verbose_name='کتاب ها')
    def __str__(self):
        return self.name+"" ""+self.family





class class_Lesson(models.Model):#کلاس هاس درس مدرسه
    name = models.CharField(max_length=100,verbose_name='enter your class name')
    students = models.ManyToManyField(student)
    def __str__(self):
        return self.name