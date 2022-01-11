"""
	intersection.py: check if two ll's intersect.
"""

# Better solution, use pointers to both heads. when both pointers
# finish traversing their own ll, they should traerse the opposite ll
# if they ever meet, return true if not false
def intersect(ll1, ll2): 
	sett = set()
	top = ll1
	while top: 
        sett.add(top)
        top = top.next

    top2 = ll2
    while top2: 
    	if top2 in sett: return top2
    	top2 = top2.next

    return None