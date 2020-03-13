#  Hint:  You may not need all of these.  Remove the unused functions.
# create hashmap
# 2 find starting point of itinery
# traverse data
# print
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# This is like real life
def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #Inserts into table
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # Sets the first destination to the starting points destination
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # after the starting point loops through the route list then sets the next destination in the list
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i - 1])

    # Returns the list of routes
    return route

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
