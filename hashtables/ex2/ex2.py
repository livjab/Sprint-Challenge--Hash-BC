#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # hash starting location is key, destination as value
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # start the route
    route = []
    route.append(hash_table_retrieve(hashtable, "NONE"))

    # go through each ticket and find next matching key value pair
    while len(route) < length:
        for ticket in tickets:
            route.append(hash_table_retrieve(hashtable, route[-1]))

    return route[:length]
