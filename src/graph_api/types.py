from graphene_django import DjangoObjectType
from pets.models import Category, Pet
from graphene import Int
from django.utils import timezone


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class PetType(DjangoObjectType):
    class Meta:
        model = Pet
    
    age = Int()

    def resolve_age(self, info):
        today =timezone.now().date()
        birth_date = self.dob.date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age