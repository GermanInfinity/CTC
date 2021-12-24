"""
    return_k.py: return kth to last in ll
"""
from LinkedList import LinkedList

def kth_to_last(node, k):
    if node is None: return None 
    slow, fast = node.head, node.head
    while k > 0: 
        if fast is None: return None
        fast = fast.next
        k -= 1

    while fast:
        fast = fast.next
        slow = slow.next

    return slow


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 9))