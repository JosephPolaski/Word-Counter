from linked_list import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
    """Unit tests for the LinkedList class"""

    def test_add_to_front(self):
        # create new LinkedList instance
        test_list = LinkedList()

        # add nodes
        test_list.add_to_front('the', 5)
        test_list.add_to_front('dog', 6)
        test_list.add_to_front('runs', 7)

        # check values
        current = test_list.head
        check_list = []

        # iterate through list
        while current is not None:
            # increment current
            previous = current
            current = current.next

            # add previous Node to list
            check_list.append(str(previous))

        self.assertLessEqual(check_list, ['{runs: 7}', '{dog: 6}', '{the: 5}'])

    def test_fetch_node(self):
        # create new LinkedList instance
        test_list = LinkedList()

        # add nodes
        test_list.add_to_front('the', 5)
        test_list.add_to_front('dog', 6)
        test_list.add_to_front('runs', 7)

        # fetch one valid key and one invalid
        dog = test_list.fetch_node('dog')
        horse = test_list.fetch_node('horse')

        self.assertEqual(dog.value, 6)
        self.assertIsNone(horse)

    def test_remove(self):
        # create new LinkedList instance
        test_list = LinkedList()

        # add nodes
        test_list.add_to_front('the', 5)
        test_list.add_to_front('dog', 6)
        test_list.add_to_front('runs', 7)

        # test list size
        self.assertEqual(test_list.size, 3)

        # remove dog
        test_list.remove('dog')

        # test list size
        self.assertEqual(test_list.size, 2)
        self.assertIsNone(test_list.fetch_node('dog'))

        # remove first element
        test_list.remove('runs')


if __name__ == "__main__":
    unittest.main()
