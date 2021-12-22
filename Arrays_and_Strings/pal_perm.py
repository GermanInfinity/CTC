"""
    Palindrom perm: check if string is a permutation of a palindrome.
"""
import unittest
from collections import Counter

def pal_perm(input_str):
    phrase = ""
    for char in input_str.lower():  
        if char != " ": 
            phrase += char

    freq = Counter(phrase)
    
    if (len(phrase) % 2): # Odd
        num_odd = 0
        for val in freq: 
            if freq[val] % 2 != 0: 
                num_odd += 1

        return True if num_odd == 1 else False

    else: 
        for val in freq: 
            if freq[val] % 2 != 0: return False
        return True
        


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    #print (pal_perm('Able was I ere I saw Elba'))
    unittest.main()


    