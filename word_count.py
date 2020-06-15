"""
Word Count

This module contains the class definition for WordCount. This class is designed to take in a .txt file
and store each unique word and the number of times it appears in the text file, into a hash map.
It will then list the words in descending order based on how many times the occurred in the document.
"""
import re
from hash_map import HashMap

# regular expression used to capture words
rgx = re.compile("(\w[\w']*\w|\w)")


def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).


    :param source: the file name containing the text
    :param number: the number of top results to return (e.g. 5 would return the 5 most common words)
    :return A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500, hash_function_2)

    # This block of code will read a file one word at a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                # convert word to lowercase to avoid inconsistent hash values
                # due to different cases of the same word.
                w = w.lower()

                # check if the current word already exists as a key
                if w in keys:
                    current_count = ht.get(w)  # fetch the current count for that word
                    current_count += 1  # increment count by one
                    ht.put(w, current_count)  # update value for the key
                else:
                    # word does not exist in hash map
                    keys.add(w)  # add current word to keys set
                    ht.put(w, 1)  # insert key into hash map with value of 1

    #  fetch unsorted list of tuples from parsed data
    word_count_list = compile_list(ht, keys)

    #  sort word count tuple list
    word_count_list = word_count_sort(word_count_list)

    # initialize and fill final word list
    final_list = []

    for index in range(0, number):
        final_list.append(word_count_list[index])

    return final_list


def compile_list(hash_map, keys):
    """
    This is a helper function for top_words() it compiles an unsorted list of tuples containing all key value pairs
    in hash_map

    :param hash_map: this is a HashMap() object that will be passed in by the top words function.
    :param keys: this is a set of keys that was generated while parsing the text file
    :return: word_counts: unsorted list of tuples of all key:value pairs in hash_map formatted (key, value)
    """
    word_counts = []  # initialize empty list for word counts

    # iterate through all keys in the set
    for key in keys:
        value = hash_map.get(key)  # fetch value for the current key
        word_counts.append((key, value))  # append the tuple formatted (key, value) to the word_counts list

    return word_counts


def word_count_sort(word_count_list):
    """
    This is an implementation of an insertion sort. It will sort the list of word count (key, value) tuples
    by value in descending order so that the word with the highest occurrence is at index 0.

    :param word_count_list: unsorted list of tuples of all key:value pairs in hash_map formatted (key, value)
    :return: word_count_list: the same list entered, but sorted in descending order.
    """

    for index in range(1, len(word_count_list)):
        # initialize pointers
        value = word_count_list[index]  # starts at the tuple in index 1
        position = index - 1  # initialize to start at 0

        # move items to a higher index position while their value is less than the value at the next index
        # compare values in tuple[1] but swap entire tuple
        while position >= 0 and word_count_list[position][1] < value[1]:
            word_count_list[position + 1] = word_count_list[position]  # swap the tuple at position into next index
            position -= 1  # decrement to fill lower index and break loop

        word_count_list[position + 1] = value  # move higher number left one index

    return word_count_list


if __name__ == "__main__":
    print(top_words("words.txt", 10))
