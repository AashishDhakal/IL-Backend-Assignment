from django.db.models import Q

import re
from itertools import groupby
from operator import itemgetter


# eq and ne are not natively supported by django ORM so adding a dict to
# map them to django ORM equivalent lookups
operation_mapping = {
    'eq': 'exact',
    'lt': 'lt',
    'gt': 'gt',
    'ne': 'exact'
}


def parse_search_phrase(allowed_fields, phrase):
    # the function to parse the search phrase
    phrase = re.sub("[()]", "", phrase)  # removing the brackets
    statements = re.split('AND | OR', phrase)  # splitting the phrase by AND
    # and OR
    query = Q()  # initiating Q query
    filters = []
    for statement in statements:
        statement = statement.strip()  # removing space at start and end if any
        # splitting up each filter condition by spaces
        statement = statement.split(" ")
        field = statement[0]  # first item will be the field name
        operation = statement[1]  # second will be the required operation
        value = statement[2]  # third will be the value to compare
        filters.append({'field':field, 'operation': operation, 'value':value})

    # Now we group each dict in the filters list by the field name to
    # distinguish if it needs to be built as either of OR/AND query
    filters = sorted(filters, key=itemgetter('field'))
    for key, value in groupby(filters, key=itemgetter('field')):
        new_query = Q()
        for k in value:
            field = k['field']
            if field not in allowed_fields:
                # if field is not in allowed list we skip
                continue
            operation = k['operation']
            value = k['value']
            mapped_operation = operation_mapping[operation]
            if operation == 'ne':
                # since we dont have equivalent lookup for not equals we use
                # negation at the beginning of eq Q query
                new_query |= ~Q(
                    **{f"{field}__{mapped_operation}": value}
                )
            else:
                new_query |= Q(
                    **{f"{field}__{mapped_operation}": value}
                )
        query &= new_query
    return query
