from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=200)
    cat_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class QueryManager(models.Manager):
    def active(self, cat_id):
        return self.filter(category__id=cat_id).filter(query_date__lte=timezone.now())



class Query(models.Model):
    query=models.TextField()
    query_date=models.DateTimeField(auto_now_add=True)
    result=models.TextField(null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    #c_objects=QueryManager()
    description=models.TextField(null=True)
    name=models.CharField(max_length=100, null=True)
    #query_date.editable=True

    def __str__(self):
        return self.name


class Track(models.Model):
    date=models.DateField(max_length=200)
    query=models.ForeignKey(Query,on_delete=models.CASCADE)
    team=models.CharField(max_length=200, null=True)
    opp=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.query.name






class cError(models.Model):
    one=models.TextField(null=True)
    two=models.TextField(null=True)






