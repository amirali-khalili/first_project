import graphene # type: ignore
from graphene_django import DjangoObjectType # type: ignore #used to change Django object into a format that is readable by GraphQL
from app.models import Contact

class ContactType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model = Contact
        field = ("id", "name", "phone_number")

class Query(graphene.ObjectType):
    #query ContactType to get list of contacts
    list_contact=graphene.List(ContactType)

    def resolve_list_contact(root, info):
        # We can easily optimize query count in the resolve method
        return Contact.objects.all()

schema = graphene.Schema(query=Query)