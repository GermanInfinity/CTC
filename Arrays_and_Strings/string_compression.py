"""
    string_compression.py: return compressed version of string
"""
import unittest
from collections import Counter
def string_compression(s): 
    # use two pointers
    if s=="": return ""

    p1, p2 = 0, 1
    res = ""
    while p1 < len(s): 
        if p2 + p1 >= len(s): 
            res += s[p1] + str(p2)
            break

        if s[p1] == s[p1 + p2]:
            p2 += 1
        elif s[p1] != s[p1 + p2]: 
            res += s[p1] + str(p2)
            p1 = p1 + p2
            p2 = 1

    return s if len(res) > len(s) else  res




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    print (string_compression("aabbdeeeea"))
    #unittest.main()