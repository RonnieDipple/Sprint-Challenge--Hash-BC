#  Hint:  You may not need all of these.  Remove the unused functions.
# create hashmap
# 2 find starting point of itinery
# traverse data
# print
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# This is like real life
def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    destination = None

    # The ticket for your first flight has a destination with a `source` of `NONE`
    # Therefore find the ticket with NONE
    for ticket in tickets:
        if ticket.source == "NONE":
            destination = ticket.destination
        # Add all the tickets into the hash_table
        hash_table_insert(hashtable, ticket.source, ticket.destination)

        # Add the new destiantion of each ticket to the route.
        for i in range(len(tickets)):
            route[i] = destination
            destination = hash_table_retrieve(hashtable, destination)

        return route[:-1]

reconstruct_trip([
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG")
], 10)
