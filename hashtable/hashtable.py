class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY
        self.buckets = [None] * capacity
        self.num_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_items / len(self.buckets)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        # find the start of the linked list using the index
        if self.buckets[index] is not None:
            # search through the linked list
            current = self.buckets[index]
            while current is not None:
                # if the key already exists
                if current.key == key:
                    # overwrite the value
                    current.value = value
                    return
                current = current.next
            # add new HashTableEntry into the head of linked list
            head = self.buckets[index]
            self.buckets[index] = HashTableEntry(key, value)
            self.num_items += 1
            self.buckets[index].next = head
        # slot is empty
        else:
            # add new HashTableEntry
            self.buckets[index] = HashTableEntry(key, value)
            self.num_items += 1

        # automatic resizing if load factor increases above 0.7
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.buckets[index] is not None:
            current = self.buckets[index]
            # if key is the current index (head)
            if current.key == key:
                # point the index to the next item in the linked list
                self.buckets[index] = current.next
                self.num_items -= 1
                return current.value
            # otherwise, search through the linked list for the key
            previous = current
            current = current.next

            while current is not None:
                # if the key exists
                if current.key == key:
                    # link the prev to next (cut out the current node)
                    previous.next = current.next
                    self.num_items -= 1
                    return current.value
                else:
                    previous = current
                    current = current.next
        return "key not found"

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current = self.buckets[index]
        while current is not None:
            # if the key exists
            if current.key == key:
                return current.value
            current = current.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # make a new array
        old_buckets = self.buckets

        # check new_capacity
        if new_capacity >= MIN_CAPACITY:
            self.capacity = new_capacity
        else:
            self.capacity = MIN_CAPACITY
        self.buckets = [None] * self.capacity
        self.num_items = 0
        # go through each linked list in the old array
        for item in old_buckets:
            current = item
            while current is not None:
                # insert the items into the new array
                self.put(current.key, current.value)
                current = current.next


if __name__ == "__main__":
    ht = HashTable(8)
    capacity_1 = ht.get_num_slots()
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    capacity_2 = ht.get_num_slots()
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    capacity_3 = ht.get_num_slots()

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    print(f"\nResized from {capacity_1} to {capacity_2} to {capacity_3}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
