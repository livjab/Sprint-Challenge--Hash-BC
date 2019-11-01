#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length > 2:

        # create hash table with weights, indices
        for weight in weights:
            hash_table_insert(ht, weight, weights.index(weight))

        # check hash table for matching weights
        summed_weights = []
        for weight in weights:
            summed_weights.append(hash_table_retrieve(ht, (limit - weight)))

        # remove Nones from list
        answer = [x for x in summed_weights if x is not None]

        return answer

    # If a pair doesn't exist, return None
    elif length == 2:
        if weights[0] + weights[1] != limit:
            return None
        else:
            return [1, 0]

    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")



weights_3 = [4, 4]
length = len(weights_3)
limit = 8
print(get_indices_of_item_weights(weights_3, length, limit))
