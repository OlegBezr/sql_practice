from django.shortcuts import render
from .models import Person, Relation
from .lib.csv_operations import *
import datetime, csv
from django.http import FileResponse
from django.http import HttpResponse, Http404
import os

def get_persons(request):
    create_persons_csv()
    file_path = 'uploads/persons.csv'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=persons.csv'
            return response
    raise Http404


def get_relations(request):
    create_relations_csv()
    file_path = 'uploads/relations.csv'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=relations.csv'
            return response
    raise Http404


def index(request):
    persons = Person.objects.all()
    relations = Relation.objects.all()

    person_ids = persons.values_list('id', flat=True) 
    relation_ids = relations.values_list('id', flat=True)

    person_fields = Person._meta.fields
    relation_fields = Relation._meta.fields

    if request.method == "POST":
        post_operation_switcher(request)

    return render(
        request,
        "sql/index.html", 
        context={
            "persons": persons,
            "person_ids": person_ids,
            "person_fields": person_fields,
            "relations": relations,
            "relation_ids": relation_ids,
            "relation_fields": relation_fields
        }
    )


def post_operation_switcher(request):
    type = request.POST.get("type")

    if type == "add_relation":
        params = request.POST
        Relation.add_relation(params)
    elif type == "update_relation":
        params = request.POST
        Relation.update_relation(params)
    elif type == "delete_relation":
        relation_id = request.POST.get("relation_id")
        if relation_id.isdigit():
            Relation.objects.filter(id=relation_id).delete()
    elif type == "update_person" or type == "add_person":
        params = { field.name: request.POST.get(field.name) for field in Person._meta.fields }
        person = Person(**params)
        person.save()
    elif type == "delete_person":
        params = { field.name: request.POST.get(field.name) for field in Person._meta.fields }
        person = Person(**params)
        person.delete()


def date_valid(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False
