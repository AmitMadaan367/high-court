from django.db import models

# Create your models here.


class CaseType(models.Model):
    Casetypes = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Casetypes)

class Department(models.Model):
    Departmens = models.CharField(max_length=200, default="", null=True,blank=True,)
    
    def __str__(self):
        return str(self.Departmens)

class Year(models.Model):
    Years = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Years)

class InternelCategory(models.Model):
    InternelCategorya = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.InternelCategorya)

class InternalCategoryCustom(models.Model):
    Category  = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Category )
class Commissions(models.Model):
    Commission = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Commission)
class ConstituionalBodies(models.Model):
    Constituional = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Constituional)

class BoardsandCorporations(models.Model):
    Boards = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Boards)

class Post(models.Model):
    Posts = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Posts)
class Advertisement(models.Model):
    Advertisements = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Advertisements)
class Cat(models.Model):
    Cats = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Cats)
class ConstituionalBodies(models.Model):
    Constituional = models.CharField(max_length=200, default="", null=True,blank=True,)
    def __str__(self):
        return str(self.Constituional)



class userinfo(models.Model):
    ids = models.AutoField(primary_key=True)

    userid = models.CharField(max_length=200, default="", null=True,blank=True,)
    casetype = models.CharField(max_length=200, default="", null=True,blank=True,)
    caseNo = models.CharField(max_length=200, default="", null=True,blank=True,)
    year_value = models.CharField(max_length=200, default="", null=True,blank=True,)
    InternelCategorys = models.CharField(max_length=200, default="", null=True,blank=True,)
    InternelCustom = models.CharField(max_length=200, default="", null=True,blank=True,)
    dprtmnt = models.CharField(max_length=200, default="", null=True,blank=True,)
    commis = models.CharField(max_length=200, default="", null=True,blank=True,)
    bodies = models.CharField(max_length=200, default="", null=True,blank=True,)
    Boards = models.CharField(max_length=200, default="", null=True,blank=True,)
    post = models.CharField(max_length=200, default="", null=True,blank=True,)
    Advertisements_year = models.CharField(max_length=200, default="", null=True,blank=True,)
    cat = models.CharField(max_length=200, default="", null=True,blank=True,)
    status = models.CharField(max_length=200, default="", null=True,blank=True,)
    copy = models.FileField(upload_to ='uploads/')
    prayer = models.CharField(max_length=200, default="", null=True,blank=True,)
    issue = models.CharField(max_length=200, default="", null=True,blank=True,)
    law = models.CharField(max_length=200, default="", null=True,blank=True,)
    nextdate = models.CharField(max_length=200, default="", null=True,blank=True,)
    lastorder = models.FileField(upload_to ='uploads/')
    def __str__(self):
        return str(self.userid)

class othersdoc(models.Model):
    # userid =  models.ForeignKey(userinfo,on_delete=models.CASCADE)
    userid = models.OneToOneField (userinfo, unique=True, editable=False, on_delete=models.CASCADE)

    othersodcs = models.FileField(upload_to ='uploads/')
    def __str__(self):
        return str(self.userid)
