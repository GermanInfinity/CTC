"""
    remove_duplicates.py: remove duplicates in ll
"""
from LinkedList import LinkedList
def remove_dups(node): 
    if node is None: return None
    ptr = node.head
    seen = set()
    seen.add(ptr.value)

    while ptr and ptr.next: 
        if ptr.next.value in seen: 
            ptr.next = ptr.next.next
        else: 
            seen.add(ptr.next.value)
            ptr = ptr.next
    return node
    

ll = LinkedList()
ll.generate(10, 1, 4)
print(ll)
remove_dups(ll)
print(ll)

# ll.generate(100, 0, 9)
# print(ll)
# remove_dups_followup(ll)
# print(ll)