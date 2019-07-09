

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
        self.count = 0
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for l in string:
        hash = ((hash << 5) + hash) + ord(l)
    return hash % max


# '''
# Fill this in.

# Hint: Use the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hash_table.count += 1
    if hash_table.storage[hash(key, hash_table.count)] == None:
        hash_table.storage[hash(key, hash_table.count)
                           ] = LinkedPair(key, value)
    else:
        def linked_list_rec(hash_table, existing_value, key, value):
            if existing_value.next == None:
                existing_value.next = LinkedPair(key, value)
            else:
                linked_list_rec(hash_table, existing_value.next, key, value)

        linked_list_rec(hash_table, hash_table.storage[hash(
            key, hash_table.count)], key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


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
