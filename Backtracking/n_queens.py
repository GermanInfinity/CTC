# n-queen: place queens on valid positions on board
# Template: is_valid_state, get_candidates, search, solve

# Don't represent board as 2d array
# keep 1d list that tracks quens position on each row
# [1, 3, 0, 2]




def solveNQueens(self, n): 
	solutions = []
	state = []
	self.search(state, solutions, n)
	return solutions


# TEMPLATE
def solve(): 
	solutions = [] 
	state = set()
	search(state, solutions)
	return solutions


def is_valid_state(state): 
	return len(state) == n

def get_candidates(state, n):
	if not state: 
		return range(n)

	# find next position
	position = len(state)
	candidates = set(range(n))
	# prune down candidates that place queen into attacks
	for row, col in enumerate(state):
		# discard column index if it's occupied
		candidates.discard(col)
		dist = position - row

		candidates.discard(col + dist)
		candidates.discard(col - dist)
    return []

def search(state, solutions, n): 
	if is_valid_state(state, n): 
		state_string = state_to_string(state)
		solutions.append(state_string)
		return 

	for candidate in get_candidates(state, n): 
		# recurse
		state.append(candidate)
		search(state, solutions, n)
		state.remove(candidate)
		state.pop()

def state_to_string(state, n):
	# ex. [1, 3, 0, 1]
	# output: [".Q..", "...Q", "Q...", "..Q."]
	ret = []
	for i in state:
		string = "." * i + 'Q' + '.' * (n-i-1)
		ret.append(string)
	return ret

