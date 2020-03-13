#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #base case if weight is below 1 end the program
    if len(weights) <= 1:
        return None

    result = [] # to store the result to be returned and printed
    table = {} # The table itself

    # Traversal bruteforce
    for i in range(0, len(weights)):
        limit_subtracted_weight = limit - weights[i]


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")



