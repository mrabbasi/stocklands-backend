from graphene import InputObjectType
from graphene import String
from graphene import ID
from graphene import Int


class PetFilter(InputObjectType):
    name = String(required=False)
    category = ID(required=False)
    min_age = Int(required=False)
    max_age = Int(required=False)