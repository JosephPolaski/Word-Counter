from hash_map import HashMap
import unittest
from random import randint


def simple_hash(key):
    """
    This is an extremely simple hash function
    it should only be used to illustrate the functioning of this program.
    It is not secure in any way. Do not use it for any real world applications.
    """
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


class TestHashMap(unittest.TestCase):
    """Unit tests for the HashMap class"""

    def setUp(self):
        self.hash_map = HashMap(10, simple_hash)
        self.test_words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

        # add enough words that all of the test words are used at least once
        for word in range(1, 100):
            index = randint(0, 8)
            word = self.test_words[index]

            # use put()
            self.hash_map.put(word, 1)

    def test_put(self):
        """tests adding elements to hash map"""
        # tests that the put method worked in the setUp
        self.assertEqual(self.hash_map.size, 9)

    def test_contains_key(self):
        """tests checking for a key"""

        result = self.hash_map.contains_key('brown')

        self.assertTrue(result)

    def test_get(self):
        """tests retrieving a value"""

        value = self.hash_map.get('fox')

        self.assertEqual(value, 1)

    def test_resize(self):
        """tests re-sizing the hash table"""

        # check capacity
        capacity_before = self.hash_map.capacity
        size_before = self.hash_map.size

        # do a resize
        self.hash_map.resize_table(50)

        # re-check capacity
        size_after = self.hash_map.size
        capacity_after = self.hash_map.capacity

        # check that number of elements is the same
        # and that the capacity is larger and equals 50
        self.assertEqual(size_before, size_after)
        self.assertGreater(capacity_after, capacity_before)
        self.assertEqual(capacity_after, 50)

    def test_empty_buckets_and_table_load(self):
        number_empty = self.hash_map.empty_buckets()
        table_load = self.hash_map.table_load()
        print(number_empty)
        print(table_load)

    def test_clear(self):
        # lear out hash map
        self.hash_map.clear()

        # test capacity and size
        self.assertEqual(self.hash_map.capacity, 10)
        self.assertEqual(self.hash_map.size, 0)


if __name__ == "__main__":
    unittest.main()
