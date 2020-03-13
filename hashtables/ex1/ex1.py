# Merging Two Packages

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable)

# Find two items whose sum of weights equals the `limit`.
# Your function will return an instance of an `Answer` tuple that has the following form:
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #base case if weight is below 1 end the program
    if len(weights) <= 1:
        return None

    result = [] # to store the result to be returned and printed
    table = {} # The table itself

    # Traversal bruteforce, loops over weight
    for i in range(0, len(weights)):
        limit_subtracted_weight = limit - weights[i]
        
        table[weights[i]] = limit_subtracted_weight
    for i in range(0, len(weights)):
        if limit - weights[i] in table:
            result.insert(0 , i)
    return result


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")



