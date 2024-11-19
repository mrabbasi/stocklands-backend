from graphene import ObjectType
from graphene import List
from pets.models import Pet
from graph_api.types import PetType
from graph_api.arguments import PetFilter
from django.utils import timezone

class Queries(ObjectType):
    pets = List(PetType, filter=PetFilter(required=False))

    def resolve_pets(root, info, filter={}):
        pets = Pet.objects.all()

        if filter.get("name"):
            pets = pets.filter(name__icontains=str(filter["name"]))

        if filter.get("category"):
            pets = pets.filter(category__id=int(filter["category"]))
        
        if filter.get("min_age"):
            min_birth_date = timezone.now().date().replace(year=timezone.now().year - int(filter["min_age"]))
            pets = pets.filter(dob__lte=min_birth_date)
        
        if filter.get("max_age"):
            max_birth_date = timezone.now().date().replace(year=timezone.now().year - int(filter["max_age"]))
            pets = pets.filter(dob__gt=max_birth_date)

        return list(pets)