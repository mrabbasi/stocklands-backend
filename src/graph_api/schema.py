from graphene import Enum
from graphene import ObjectType
from graphene import Schema

from graph_api.mutations import Mutations
from graph_api.queries import Queries


class Query(Queries, ObjectType):
    """Top-level query object for gql endpoint"""


class Mutation(Mutations, ObjectType):
    """Top-level mutation object for gql endpoint"""


schema = Schema(
    query=Query,
    mutation=Mutation,
)
