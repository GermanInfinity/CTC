"""
	intersection.py: check if two ll's intersect.
"""
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