

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for l in string:
        hash = ((hash << 5) + hash) + ord(l)
    return (hash & 0xFFFFFFFF) % max


# '''
# Fill this in.

# Hint: Use the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    if hash_table.storage[hash(key, hash_table.capacity)] == None or hash_table.storage[hash(key, hash_table.capacity)].key == key:
        hash_table.storage[hash(key, hash_table.capacity)
                           ] = LinkedPair(key, value)
    else:
        def linked_list_rec(hash_table, current_pair, key, value):
            if current_pair.next == None:
                current_pair.next = LinkedPair(key, value)
            else:
                linked_list_rec(hash_table, current_pair.next, key, value)

        linked_list_rec(hash_table, hash_table.storage[hash(
            key, hash_table.capacity)], key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    if hash_table.storage[hash(key, hash_table.capacity)] == None:
        print('Warning: supplied key does not exist')
    elif hash_table.storage[hash(key, hash_table.capacity)].key == key:
        hash_table.storage[hash(key, hash_table.capacity)] = hash_table.storage[hash(
            key, hash_table.capacity)].next
    else:
        def linked_list_rec(hash_table, current_pair, key):
            if current_pair.next == None:
                print('Warning: supplied key does not exist')
                return
            elif current_pair.next.key == key:
                current_pair.next = current_pair.next.next
                return
            else:
                linked_list_rec(hash_table, current_pair.next, key)
        linked_list_rec(hash_table, hash_table.storage[hash(
            key, hash_table.capacity)], key)

# '''
# Fill this in.

# Should return None if the key is not found.
# '''


def hash_table_retrieve(hash_table, key):
    return_value = None
    # print('hash(key, hash_table.capacity):',
    #       hash(key, hash_table.capacity))
    if hash_table.storage[hash(key, hash_table.capacity)] != None:
        def linked_list_rec(hash_table, current_pair, key):
            nonlocal return_value
            # print('current_pair.key, key: ', current_pair.key, key)
            if current_pair.key == key:
                # print('success?', current_pair.value)
                return_value = current_pair.value
                # print('return_value: ', return_value)
            elif current_pair.next != None:
                linked_list_rec(hash_table, current_pair.next, key)
            else:
                return
        linked_list_rec(hash_table, hash_table.storage[hash(
            key, hash_table.capacity)], key)

    return return_value

# '''
# Fill this in
# '''


def hash_table_resize(hash_table):
    temp_table = HashTable(hash_table.capacity * 2)

    for slot in hash_table.storage:
        if slot != None:
            def linked_list_rec(hash_table, current_pair):
                nonlocal temp_table
                hash_table_insert(
                    temp_table, current_pair.key, current_pair.value)
                if current_pair.next != None:
                    linked_list_rec(hash_table, current_pair.next)
                else:
                    return
            linked_list_rec(hash_table, slot)

    return temp_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
