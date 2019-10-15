#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    t = ht.storage
    prelim__answer = []

    for i, w in enumerate(weights):
        retrieve = hash_table_retrieve(ht, w)
        if retrieve != None:
            if limit - weights[retrieve] == w:
                prelim__answer.append(i)
                prelim__answer.append(retrieve)

        else:
            hash_table_insert(ht, w, i)

    if len(prelim__answer) == 2:
        prelim__answer.sort(reverse=True)
        return (prelim__answer[0], prelim__answer[1])

    for n in range(0, len(t) - 1):
        if t[n] !=None:
            search_num = limit - t[n].key
            answer = hash_table_retrieve(ht, search_num)
            if answer != None:
                prelim__answer.append(answer)

    if len(prelim__answer) == 2:
        prelim__answer.sort(reverse=True)
        return (prelim__answer[0], prelim__answer[1])

    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
