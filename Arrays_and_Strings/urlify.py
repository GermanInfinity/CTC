"""
    URLify: replace " " with "%20" in a string.
"""
import unittest

# space: O(n) time: O(n)
def urlify(input_lis, i): 
    out = 0
    res = []
    for i in reversed(input_lis): 
        if i == " ": out += 1
        else: break

    for i in range(len(input_lis)-out): 
        if input_lis[i] == " ": 
            res.append('%')
            res.append('2')
            res.append('0')
            continue
        res.append(input_lis[i])

    return res

# space: O(1) time: O(n)
def urilify(inp, i): 
    p1, p2 = len(inp) - 1, i - 1

    while p1 >= 0 and p2 >= 0: 
        if inp[p1] == " ": 
            inp[p1] = inp[p2]
            p1 -= 1
            p2 -= 1
        else: 
            for i in reversed("%20"): 
                s[p1] = i
                p1 -= 1
            p2 -= 1

    return out 


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":

    #print (urlify(['h', 'i', ' ', 'b', 'u', 'd', ' ', ' '], 6))
    unittest.main()