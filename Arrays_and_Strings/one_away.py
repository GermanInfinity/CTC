"""
    One Away: check if strings need one edit away. 
"""
import unittest

# O(N) - two pointers
def one_away(str1, str2): 
    if abs((len(str1)) - len(str2)) > 1: return False

    p1, p2 = 0, 0 
    made_edit = False
    while p1 < len(str1) and p2 < len(str2): 
        if str1[p1] == str2[p2]: 
            p1 += 1
            p2 += 1
        elif not made_edit:
            made_edit = True 
            if len(str1) == len(str2): 
                p1 += 1
                p2 += 1
            elif len(str1) > len(str2): 
                p1 += 1
            else: 
                p2 += 1
        else: 
            return False
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    #print (one_away('pale', 'pas'))
    unittest.main()