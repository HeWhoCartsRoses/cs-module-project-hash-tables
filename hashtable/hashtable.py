class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.next = None


class HashTableEntry:
    def __init__(self):
        self.head = None

    def add(self, val, key):
        new = Node(val, key)
        new.next = self.head
        self.head = new

    def get(self, key):
        temp = self.head
        while(temp):
            if temp.key == key:
                return temp.data
            temp = temp.next
        return None

    def delete(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.key == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.key == key:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
        temp = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        self.table = dict.fromkeys(range(self.capacity))

    def get_num_slots(self):
        # Your code here
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash*33)+ord(c)
        return hash

    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        # Your code here
        new = self.hash_index(key)
        # old = self.table[new]
        if self.table[new] != None:
            self.table[new].add(value, key)
        else:
            lst = HashTableEntry()
            lst.add(value, key)
            self.table[new] = lst

    def delete(self, key):
        # Your code here
        i = self.hash_index(key)
        self.table[i].delete(key)

    def get(self, key):
        # Your code here
        i = self.hash_index(key)
        x = self.table[i].get(key)
        return x

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


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
