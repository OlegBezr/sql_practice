from django.db import models


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)


class Relation(models.Model):
    id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, related_name='person_id', on_delete=models.CASCADE)
    child = models.ForeignKey(Person, related_name='child_id', on_delete=models.CASCADE)

    def update_relation(params):
        relation_id = params.get("relation_id")
        person_id = params.get("person_id")
        child_id = params.get("child_id")
        if relation_id.isdigit() and person_id.isdigit() and child_id.isdigit():
            parent = Relation.objects.get(id=relation_id)
            parent.child_id = child_id
            parent.person_id = person_id
            parent.save()
    
    def add_relation(params):
        person_id = params.get("person_id")
        child_id = params.get("child_id")
        if person_id.isdigit() and child_id.isdigit():
            person = Person.objects.get(id = person_id)
            child = Person.objects.get(id = child_id)
            relation = Relation(person = person, child = child)
            relation.save()
