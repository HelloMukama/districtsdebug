from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
   
    def __str__(self):
        return self.name


class TownType(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
   
    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    town_type = models.ForeignKey(TownType, on_delete=models.SET_NULL, blank=False, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return self.name


class District(models.Model):
    city = models.ForeignKey(City, blank=False, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    town = models.ForeignKey(Town, blank=True, null=True, on_delete=models.CASCADE, related_name='commitments')
    language = models.CharField(max_length=20, blank=True)
    date_made = models.DateTimeField(blank=True, null=True)
   
    def __str__(self):
        return self.title

