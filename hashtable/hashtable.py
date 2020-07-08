
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        # self.key = key
        # self.value = value
        self.head = self.Node((key, value))

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def find(self, key):
        node = self.head
        while node is not None:
            if node.value[0] == key:
                return node.value[1]
            node = node.next
        return None

    def insert_at_head(self, key, value):
        new_node = self.Node((key, value))
        new_node.next = self.head
        self.head = new_node

    def append(self, key, value):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        new_node = self.Node((key, value))
        cur_node.next = new_node

    def delete(self, key):
        if self.head.value[0] == key:
            del_node = self.head
            self.head = self.head.next
            return del_node

        node = self.head
        while node.next is not None:
            if node.next.value[0] == key:
                del_node = node.next
                del_node.next = None
                node.next = node.next.next
                return del_node
            node = node.next

    def get_as_array(self):
        array = []
        node = self.head
        while node is not None:
            array.append((node.value[0], node.value[1]))
            node = node.next
        return array

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.pairs = 0
        self.buckets = [None for i in range(capacity)]

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.pairs/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hash = 0xcbf29ce484222325
        prime = 0x100000001b3
        if not isinstance(key, bytes):
            key = key.encode("UTF-8", "ignore")
        for byte in key:
            hash ^= byte
            hash *= prime
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        pass



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        if self.get_load_factor() >= 0.7:
            print(f"{self.get_load_factor()}")
            self.resize(self.capacity*2)
        i = self.hash_index(key)
        if self.buckets[i] is None:
            self.buckets[i] = HashTableEntry(key, value)
        else:
            self.buckets[i].insert_at_head(key, value)
        self.pairs += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        if isinstance(self.buckets[i], HashTableEntry):
            node = self.buckets[i].delete(key)
            if node == None:
                print(f"{key} node found.")
            else:
                self.pairs -= 1
            if self.buckets[i].head == None:
                self.buckets[i] = None
        if self.get_load_factor() <= 0.2:
            self.resize(self.capacity//2)



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        if isinstance(self.buckets[i], HashTableEntry):
            return self.buckets[i].find(key)
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_values = []

        for i in self.buckets:
            if not isinstance(i, HashTableEntry):
                continue
            else:
                new_values = i.get_as_array()
                old_values.extend(new_values)
        self.capacity = new_capacity
        self.buckets = [None for i in range(self.capacity)]
        for i in old_values:
            self.put(i[0], i[1])



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
