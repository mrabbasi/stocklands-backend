from graphene import ObjectType
from graphene import Mutation
from graphene import ID
from graphene import String
from graphene import Boolean
from graphene import List
from graphql import GraphQLError

from pets.models import Pet

class ErrorType(ObjectType):
    field = String()
    message = String()

class UpdatePet(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String(required=False)
        available = Boolean(required=False)

    success = Boolean()
    errors = List(ErrorType)

    def mutate(self, info, id, name, available):
        try:
            pet = Pet.objects.get(id=id)
            if not pet.available:
                return UpdatePet(success=False, errors=[ErrorType(field="available", message="This pet is not available for updates.")])
            if name:
                pet.name = name
            if available is not None:
                pet.available = available
            pet.save()
            return UpdatePet(success=True, errors=None)
        except Pet.DoesNotExist:
            return UpdatePet(success=False, errors=[ErrorType(field="id", message=f"Pet with id {id} does not exist.")])
        except Exception as e:
            return UpdatePet(success=False, errors=[ErrorType(field="general", message=str(e))])

class Mutations(ObjectType):
    update_pet = UpdatePet.Field()