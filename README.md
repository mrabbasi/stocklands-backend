# pet-planet-backend

## Contributing

### Virtual Environments

If you are wishing to contribute to this package, we strongly encourage you to
use a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You can deactivate this virtual environment at any time:

```bash
deactivate
```

### Development

Run this command to have the server automatically detect changes to the code:

```bash
make local
```

An easy way to view and test API endpoints is using Graphqli on http://localhost:8000/api/graphql

### DB Migrations

```bash
cd src && python manage.py makemigrations
cd src && python manage.py migrate
```

### Graphene Django

We highly recommend to go through the graphene django tutorial to understand how to use the library
https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain

- All queries are defined in the `queries.py` file
- All mutations are defined in the `mutations.py` file

### Objectives

You can find all the predefined queries and mutations in the `queries.py` and `mutations.py` files. We want to add some new features to the API:

1. Add a filter to the pets query to filter by age. We currently have a query to get all pets and filter by pet's name and category, but we want to be able to filter by age.
2. Only allow to update the pet if pet.available == True. We already implemented the mutation to update the pet, but we want to add a validation to only allow the update if the pet is available.
3. Make the name filter to search for a substring and case insensitive. The name filter is currently case sensitive and only searches for the exact name. We want to make it case insensitive and search for any occurrence of the name.
