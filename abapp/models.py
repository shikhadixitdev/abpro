from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Emp(CommonInfo):
    salary = models.IntegerField()


class Customer(CommonInfo):
    sales = models.IntegerField()


class Student(CommonInfo):
    fee = models.IntegerField()


# Create your models here.
