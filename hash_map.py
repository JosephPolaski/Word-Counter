"""
Hash Map

This module contains a hash map. This data structure has been designed to use chaining in order to avoid collisions.
Linked lists are used at each bucket to store nodes.
"""
from linked_list import LinkedList


class HashMap:
    """
        This is a hash map that uses chaining to avoid collisions. The LinkList class defined in
        linked_list.py is used at each bucket to hold Nodes.
    """

    def __init__(self, capacity, function):
        """
        Creates a HashMap class object.

        :param capacity: integer number of buckets available in the Hashmap
        :param function: The hashing function used to determine index locations
        """
        self.__buckets = []
        self.capacity = capacity
        self.size = 0  # represents total number of elements in the hash map
        self.__hash_func = function

        # initialize hash map with specified number of buckets
        # insert an empty LinkedList at each bucket
        for i in range(capacity):
            self.__buckets.append(LinkedList())

    def __str__(self):
        """Overrides the default __str__ method """

    def clear(self):
        """
        Completely empties all elements from the hash map
        and resets it at the current capacity.
        """
        # empty all buckets
        self.__buckets = []

        # re-initialize with empty linked lists at current capacity
        for i in range(self.capacity):
            self.__buckets.append(LinkedList())

        self.size = 0  # reset size

    def calculate_index(self, key):
        """
        This is a helper method created to calculate  a link index in order to reduce code redundancy

        :return table_index
        """
        # Calculate index the link is located at.
        hash_key = self.__hash_func(key)  # generate hash key
        table_index = hash_key % self.capacity  # convert to bucket index

        return table_index

    def contains_key(self, key):
        """
        Searches to see if a key exists within the hash table

        :return True if the key is found False otherwise
        """
        # calculate table index of desired link
        table_index = self.calculate_index(key)

        # check if the key exists at that index, if it exists return True
        if self.__buckets[table_index].fetch_node(key) is not None:
            return True
        else:
            return False

    def get(self, key):
        """
        Returns the matching value with the given key.

        :param key: the value of the key to look for
        :return The value associated to the key. None if the link isn't found.
        """

        # If the link doesnt exist return None
        if not self.contains_key(key):
            return None

        # the link does exist
        # calculate table index where link should be located
        table_index = self.calculate_index(key)

        # Fetch node with desired key and return its value
        key_node = self.__buckets[table_index].fetch_node(key)
        return key_node.value

    def resize_table(self, capacity):
        """
        Re-sizes the hash table to have a number of buckets equal to the given
        capacity. All elements are rehashed after resizing

        :param capacity: the new number of buckets.
        """
        # create a temporary list of the given capacity
        temp_list = []
        self.capacity = capacity  # update capacity

        # fill the temp list with LinkedList() objects doubling capacity
        for i in range(capacity):
            temp_list.append(LinkedList())

        # iterate through current buckets
        for bucket in self.__buckets:

            # check if the list at the current bucket contains any links
            if bucket.size > 0:

                # iterate through all links in the current bucket
                # set pointers
                previous = None
                current = bucket.head

                while current is not None:
                    # iterate pointers
                    previous = current
                    current = current.next

                    # re - hash element
                    hash_key = self.__hash_func(previous.key)  # generate hash key
                    table_index = hash_key % self.capacity  # convert to integer index

                    # add to temp list and newly hashed index
                    temp_list[table_index].add_to_front(previous.key, previous.value)

        # all links have been rehashed and added
        # set self._buckets to the new list
        self.__buckets = temp_list

    def put(self, key, value):
        """
        This method will add a key/value pair Node to the hash map. If a node with the given key
        already exists, it will simply update its value.

        :param key: the key being added or updated. (This represents a word in the word count)
        :param value: the value associated with the entry (This represents the count in the word count)
        """
        # calculate table index where link should be inserted
        table_index = self.calculate_index(key)

        # Fetch node of key if it already exists
        key_exists = self.__buckets[table_index].fetch_node(key)

        # if the key node is returned update its value
        if key_exists is not None:
            key_exists.value = value
        else:
            # if the key doesn't exist add a new node with the key and value given
            self.__buckets[table_index].add_to_front(key, value)
            self.size += 1
        return

    def remove(self, key):
        """
        Removes an element with the given key if it exists. If it doesn't exist
        the method returns with no action taken.

        :param key: they key to search for and remove along with its value
        """
        # calculate table index of desired link
        table_index = self.calculate_index(key)

        # check if the node exists, if key is not found exit.
        if not self.contains_key(key):
            return

        # remove node with matching key
        self.__buckets[table_index].remove(key)
        self.size -= 1

    def empty_buckets(self):
        """
        Counts the number of unused (empty) buckets in the table

        :return bucket_count: The number of empty buckets
        """
        # initialize count variable
        bucket_count = 0

        # iterate through buckets and count empty ones
        for bucket in self.__buckets:

            # if the linked list at bucket is empty increment bucket_count
            if bucket.size == 0:
                bucket_count += 1

        return bucket_count

    def table_load(self):
        """
        Calculates the load factor of the hash map

        :return load_factor: the ratio of (number of links) / (number of buckets) in the table as a float.
        """
        num_of_links = 0  # keeps track of total number of links

        # iterate through buckets and sum the number of links
        for bucket in self.__buckets:
            num_of_links += bucket.size

        # divide number of links by number of buckets
        load_factor = float(num_of_links / self.capacity)
        return load_factor

