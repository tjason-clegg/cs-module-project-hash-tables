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
    A hash table that starts with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Set the length of the table to capacity
        self.capacity = capacity
        self.table = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        total = 0

        for key in self.table:
            if key is not None:
                total += 1

        return total / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5831

        for c in key:
            # By using 33, we can spread the numbers evenly
            hash = (hash * 33) + ord(c)
        return hash

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
        # Your code here

        # Index for table
        index = self.hash_index(key)
        return self.insert_at_head(key, value, index)

    def insert_at_head(self, key, value, index):
        # Create new node
        node = HashTableEntry(key, value)

        # If entry at index is empty, assign node as head
        if self.table[index] is None:
            self.table[index] = node
        # If not empty, swap current head and new node
        else:
            node.next = self.table[index]
            self.table[index] = node

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # We dont want to erase the index since we want to keep it, but for it to not hav an assigned value
        current = self.table[index]

        if current.key == key:
            self.table[index] = self.table[index].next
            return self.table[index]

        prev = current
        current = current.next

        while current is not None:
            # if current key is key, change prev.next to current.next. Current node will be deleted
            if current.key == key:
                prev.next = current.next
                return current.value

            else:
                prev = prev.next
                current = current.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # Return the searched index using the key
        return self.find(key, index)

    def find(self, key, index):

        current = self.table[index]
        # loop to check chain links in index
        while current is not None:
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
        # Your code here

        # Set new capacity
        self.capacity = new_capacity

        # Copy of old table
        old_table = self.table

        # Changing capacity of table
        self.table = [None] * self.capacity

        for i in old_table:
            self.put(i.key, i.value)

            current = i.next
            # Loop to go through chain links at current index if applicable
            while current is not None:
                self.put(current.key, current.value)

                current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
