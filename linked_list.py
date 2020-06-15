"""
Linked List

This module contains a simplified singly-linked list. This data structure has been designed for use in chaining for the
HashMap() class in hash_map.py. It only contains the add_to_front(), remove() and contains() methods.
"""


class Node:
    """This class represents a node in the LinkedList Class"""

    def __init__(self, key, value):
        # data members
        self.key = key
        self.value = value

        # next pointer
        self.next = None

    def __str__(self):
        """overrides __str__ method"""
        return '{' + str(self.key) + ': ' + str(self.value) + '}'


class LinkedList:
    """
    This is a simplified singly-linked list

    Contains 3 methods:
        - add_to_front( key, value): adds a Node with the key, value pair to the front of the list.
        - remove(key): removes Node with the matching key specified by argument.
        - fetch_node(key): searches for a Node with the matching Key
    """

    def __init__(self):
        self.head = None;
        self.size = 0;  # keeps track of number of elements in the linked list

    def add_to_front(self, key, value):
        """
        Adds a Node object with the specified key and value to the front of the linked list.

        :param key: this will be a string type variable representing a word in the words.txt file
        :param value: this will be an integer variable representing the number of instances of the key in the .txt file
        """

        # create a new node object with the given key and value.
        new_node = Node(key, value)

        # insert new node to front of list
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def fetch_node(self, key):
        """
        Searches for a Node with the matching key.

        :param key: this will be a string type variable representing a word in the words.txt file
        :return: returns the Node if it exists or None if it doesnt exist
        """
        current = self.head

        while current is not None:
            previous = current
            current = current.next

            if previous.key == key:
                return previous

        return None

    def remove(self, key):
        """
        Removes a node from the list if it exists.

        :param key: this will be a string type variable representing a word in the words.txt file
        """
        # list is empty: exit
        if self.head is None:
            return False

        # best case: first element is a match
        if self.head.key == key:
            self.head = self.head
            self.size -= 1
            return True

        # search for Node
        previous = self.head
        current = self.head.next

        while current is not None:
            # check for key match
            if current.key == key:
                previous.next = current.next    # remove node from list
                self.size -= 1
                return True

            # no match, iterate linked list pointers
            previous = current
            current = current.next
