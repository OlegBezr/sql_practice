from django.db import models


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)


class Relation(models.Model):
    person_id = models.ForeignKey(Person, related_name='person_id', on_delete=models.CASCADE)
    child_id = models.ForeignKey(Person, related_name='child_id', on_delete=models.CASCADE)
