INITIAL_CAPACITY = 37


# In a more complex hash table implementation (i.e. an open-addressed, double-hashed hash table),
# it’s important that the capacity is prime, and that it can be changed.
# On the other hand, our separate chaining hash table sets the capacity once and never changes it,
# regardless of how many elements are stored.
# This is good for simplicity, but bad for scalability.


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY  # determine the size of our internal array
        self.size = 0  # the number of elements that have been inserted
        self.buckets = [None] * self.capacity  # the internal array,
        # storing each inserted value in a “bucket” based on the provided key

    def __str__(self):
        return str(self.buckets)

    def hash(self, key):
        key = str(key)
        hashsum = 0
        # For each character in the key
        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            hashsum += (idx + len(key)) ** ord(
                c)  # Python ord() function takes string argument of a single Unicode character
            # and return its integer Unicode code point value. The valid range for the argument is from 0 through 1,114,111
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        # 2. Compute index of key
        index = self.hash(key)
        # Go to the node corresponding to the hash
        node = self.buckets[index]
        # print('self.buckets[index]', self.buckets[index])
        # 3. If bucket is empty:
        if node is None:
            self.size += 1
            # Create node, add it, return
            self.buckets[index] = Node(key, value)
            # print(index, node)
            return
        # 4. Collision! Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:  # итерируемся по нодам
            if node.key == key: # чтобы не пихать одно и то же. для некоторых задач эту часть нужно убрать
                node.value = value
                return
            prev = node
            node = node.next
        # Add a new node at the end of the list with provided key/value
        self.size += 1
        prev.next = Node(key, value)

    def find(self, key):
        # 1. Compute hash
        index = self.hash(key)
        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value

    def remove(self, key):
        # 1. Compute hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        # 2. Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none
        if node is None:
            # 3. Key not found
            return None
        else:
            # 4. The key was found.
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            if prev is None:
                self.buckets[index] = node.next  # May be None, or the next match
            else:
                prev.next = node.next
                # prev.next = prev.next.next  # LinkedList delete by skipping over
            # Return the deleted result
            return result


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Node has a next field because it’s actually part of a LinkedList.
        # Because the hash table uses separate chaining,
        # each bucket will actually contain a LinkedList of nodes containing the objects stored at that index.
        # This is one method of collision resolution.

    def __str__(self):
        temp_node = self
        node_list = []
        while temp_node is not None:
            node_list.append(
                ("<Node: (%s, %s), next: %s>" % (temp_node.key, temp_node.value, temp_node.next is not None)), )
            temp_node = temp_node.next
        return str(node_list)

    def __repr__(self):
        return str(self)


ht = HashTable()
list_str = []
for num in range(1200, 1210):
    temp_str = str(num) + chr(num)
    list_str.append(temp_str)

for future_value, future_key in enumerate(list_str):
    print(future_key, future_value)
    ht.insert(future_key, future_value)
print(ht)
print(ht.size)
print('--------')
ht.insert('1209', 77)
print(ht)
print(ht.size)
