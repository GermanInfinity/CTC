"""
	check_permutation.py: given two strings, determine if one is a permutation
						  of the other. 
"""

import unittest
from collections import Counter

# time: O(n) space: O(n) with a dictionary 
def check_permutation2(str1, str2):
	if len(str1) != len(str2): return False
	str1_count = Counter(str1)
	str2_count = Counter(str2)

	for char in str1: 
		if str1_count[char] != str2_count[char]: return False
	return True

# time: O(n) space: O(n) with a dictionary  (different implementation)
def check_permutation(str1, str2):
	if len(str1) != len(str2): return False
	str1_count = {}
	for ele in str1: 
		str1_count[ele] = str1_count.get(ele, 0) + 1

	for char in str2: 
		if char not in str1: return False
		str1_count[char] -= 1
		if str1_count[char] == 0: del str1_count[char]


	return len(str1_count) == 0 #True if len(str1_count) == 0 else False



class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
