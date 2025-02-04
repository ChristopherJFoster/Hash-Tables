import copy

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
        self.count = 0

    def resize_up(self):
        temp_storage = copy.deepcopy(self.storage)
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        self.count = 0

        for slot in temp_storage:
            if slot != None:
                def linked_list_rec(hash_table, current_pair):
                    hash_table_insert(
                        self, current_pair.key, current_pair.value, True)
                    if current_pair.next != None:
                        linked_list_rec(hash_table, current_pair.next)
                    else:
                        return
                linked_list_rec(self, slot)

    def resize_down(self):
        temp_storage = copy.deepcopy(self.storage)
        self.capacity = int(self.capacity / 2)
        self.storage = [None] * self.capacity
        self.count = 0

        for slot in temp_storage:
            if slot != None:
                def linked_list_rec(hash_table, current_pair):
                    hash_table_insert(
                        self, current_pair.key, current_pair.value, True)
                    if current_pair.next != None:
                        linked_list_rec(hash_table, current_pair.next)
                    else:
                        return
                linked_list_rec(self, slot)

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
def hash_table_insert(hash_table, key, value, resize=False):
    hash_table.count += 1
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

    if resize == False and hash_table.count / hash_table.capacity > 0.7:
        print(hash_table.count / hash_table.capacity, 'up!')
        hash_table.resize_up()


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    if hash_table.storage[hash(key, hash_table.capacity)] == None:
        print('Warning: supplied key does not exist')
    elif hash_table.storage[hash(key, hash_table.capacity)].key == key:
        hash_table.count -= 1
        hash_table.storage[hash(key, hash_table.capacity)] = hash_table.storage[hash(
            key, hash_table.capacity)].next
    else:
        def linked_list_rec(hash_table, current_pair, key):
            if current_pair.next == None:
                print('Warning: supplied key does not exist')
                return
            elif current_pair.next.key == key:
                hash_table.count -= 1
                current_pair.next = current_pair.next.next
                return
            else:
                linked_list_rec(hash_table, current_pair.next, key)
        linked_list_rec(hash_table, hash_table.storage[hash(
            key, hash_table.capacity)], key)

    if hash_table.count / hash_table.capacity < 0.2:
        print(hash_table.count / hash_table.capacity, 'down!')
        hash_table.resize_down()

# '''
# Fill this in.

# Should return None if the key is not found.
# '''


def hash_table_retrieve(hash_table, key):
    return_value = None
    if hash_table.storage[hash(key, hash_table.capacity)] != None:
        def linked_list_rec(hash_table, current_pair, key):
            nonlocal return_value
            if current_pair.key == key:
                return_value = current_pair.value
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
                    temp_table, current_pair.key, current_pair.value, True)
                if current_pair.next != None:
                    linked_list_rec(hash_table, current_pair.next)
                else:
                    return
            linked_list_rec(hash_table, slot)

    return temp_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    print('count: ', ht.count, 'capacity: ', ht.capacity)
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    print('count: ', ht.count, 'capacity: ', ht.capacity)
    hash_table_insert(ht, "line_3", "Linked list saves the day!")
    print('count: ', ht.count, 'capacity: ', ht.capacity)

    hash_table_remove(ht, "line_2")
    print('count: ', ht.count, 'capacity: ', ht.capacity)
    hash_table_remove(ht, "line_3")
    print('count: ', ht.count, 'capacity: ', ht.capacity)

    # print(hash_table_retrieve(ht, "line_1"))
    # print(hash_table_retrieve(ht, "line_2"))
    # print(hash_table_retrieve(ht, "line_3"))

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
