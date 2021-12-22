"""
	string_rotation: check if one string is rotation of other string.
"""
import unittest
def string_rotation(s1, s2): 
	if len(s1) != len(s2): return 0
	p1, p2 = 0, 1
	while p2 < len(s1):
		if s1[:p2] + s1[p2:] ==  s2[p2:] + s2[:p2]:
			
			


	if p1 == len(s1) - 1: return True
	return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        #('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()