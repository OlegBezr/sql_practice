from ..models import Person, Relation
import csv

def create_persons_csv():
    with open('uploads/persons.csv', 'w', newline='') as csvfile:
        userwriter = csv.writer(csvfile, delimiter=',')
        persons = Person.objects.all()
        for user in persons:
            row = (user.id, user.name, user.gender, user.birth_date)
            userwriter.writerow(row)


def create_relations_csv():
    with open('uploads/relations.csv', 'w', newline='') as csvfile:
        parentwriter = csv.writer(csvfile, delimiter=',')
        relations = Relation.objects.all()
        for parent in relations:
            row = (parent.person_id, parent.child_id)
            parentwriter.writerow(row)