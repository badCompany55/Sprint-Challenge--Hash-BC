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
    ht = HashTable(length)
    route = [None] * length

    for t in tickets:
        hash_table_insert(ht, t.source, t.destination)

    destination = hash_table_retrieve(ht, "NONE")
    route[0] = destination

    for i in range(1, length):
        destination = hash_table_retrieve(ht, destination)
        route[i] = destination

    return route
