"""
    is_unique: implement an algorithm to determine if a string has all unique
            elements.
"""

import unittest
from collections import Counter

# time: O(n), space: O(n)
def unique(input): 
    store = Counter(input)

    for ele in store: 
        if store[ele] > 1: return False
    return True

# time: O(nlogn), space: O(n)
def unique_2(input_str): 
    input_str = sorted(input_str)

    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i + 1]: return False
    return True

# time: O(n), space: O(n). use a set 
def unique_3(input): 
    return True if len(set(input)) == len(input) else False



class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique_2(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique_2(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    # print (unique_2("23ds2"))
    unittest.main()