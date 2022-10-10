from random import choices
from django.db import models



class SystemAnalyst(models.Model):
    Name = models.CharField(max_length = 200)
    EmployeeID = models.IntegerField(default=0)

    class HOURS(models.IntegerChoices):
        PART = 20, "PART TIME 50%"
        PARTTWO = 30, "PART TIME 75%"
        FULL = 40, "FULL TIME"
        LEAD = 44, "TEAM LEAD"
    
    hoursworking = models.PositiveSmallIntegerField(
        choices = HOURS.choices, default = HOURS.FULL
    )

    def __str__(self):
        return self.Name
    
    def MonthlySalary(self):
            return self.hoursworking * 15

class SoftwareTester(models.Model):
    Name = models.CharField(max_length = 200)
    EmployeeID = models.IntegerField(default=0)

    class HOURS(models.IntegerChoices):
        PART = 20, "PART TIME 50%"
        PARTTWO = 30, "PART TIME 75%"
        FULL = 40, "FULL TIME"
        LEAD = 44, "TEAM LEAD"
    
    hoursworking = models.PositiveSmallIntegerField(
        choices = HOURS.choices, default = HOURS.FULL
    )

    def __str__(self):
        return self.Name

    def MonthlySalary(self):
       return self.hoursworking * 15


class DataScientist(models.Model):
    Name = models.CharField(max_length = 200)
    EmployeeID = models.IntegerField(default=0)
    
    class HOURS(models.IntegerChoices):
        PART = 20, "PART TIME 50%"
        PARTTWO = 30, "PART TIME 75%"
        FULL = 40, "FULL TIME"
        LEAD = 44, "TEAM LEAD"
    
    hoursworking = models.PositiveSmallIntegerField(
        choices = HOURS.choices, default = HOURS.FULL
    )

    def __str__(self):
        return self.Name

    def MonthlySalary(self):
       return self.hoursworking * 15


class BackEnd(models.Model):
    Name = models.CharField(max_length = 200)
    EmployeeID = models.IntegerField(default=0)
    
    class HOURS(models.IntegerChoices):
        PART = 20, "PART TIME 50%"
        PARTTWO = 30, "PART TIME 75%"
        FULL = 40, "FULL TIME"
        LEAD = 44, "TEAM LEAD"
    
    hoursworking = models.PositiveSmallIntegerField(
        choices = HOURS.choices, default = HOURS.FULL
    )

    def __str__(self):
        return self.Name

    def MonthlySalary(self):
       return self.hoursworking * 15

class FrontEnd(models.Model):
    Name = models.CharField(max_length = 200)
    EmployeeID = models.IntegerField(default=0)
    
    class HOURS(models.IntegerChoices):
        PART = 20, "PART TIME 50%"
        PARTTWO = 30, "PART TIME 75%"
        FULL = 40, "FULL TIME"
        LEAD = 44, "TEAM LEAD"
    
    hoursworking = models.PositiveSmallIntegerField(
        choices = HOURS.choices, default = HOURS.FULL
    )

    def __str__(self):
        return self.Name

    def MonthlySalary(self):
       return self.hoursworking * 15


class UiUx(models.Model):
    Name = models.CharField(max_length = 200)
    EmployeeID = models.IntegerField(default=0)
    
    class HOURS(models.IntegerChoices):
        PART = 20, "PART TIME 50%"
        PARTTWO = 30, "PART TIME 75%"
        FULL = 40, "FULL TIME"
        LEAD = 44, "TEAM LEAD"
    
    hoursworking = models.PositiveSmallIntegerField(
        choices = HOURS.choices, default = HOURS.FULL
    )

    def __str__(self):
        return self.Name

    def MonthlySalary(self):
       return self.hoursworking * 15


class SalesMarketing(models.Model):
    Name = models.CharField(max_length = 200)
    EmployeeID = models.IntegerField(default=0)
    
    class HOURS(models.IntegerChoices):
        PART = 20, "PART TIME 50%"
        PARTTWO = 30, "PART TIME 75%"
        FULL = 40, "FULL TIME"
        LEAD = 44, "TEAM LEAD"
    
    hoursworking = models.PositiveSmallIntegerField(
        choices = HOURS.choices, default = HOURS.FULL
    )

    def __str__(self):
        return self.Name

    def MonthlySalary(self):
       return self.hoursworking * 15