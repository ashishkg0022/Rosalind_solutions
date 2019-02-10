

def generate_set(multiset):

	multiset = sorted(multiset)
	X = [0] # we assume 0 to be always there

	X.append(max(multiset))

	multiset.remove(max(multiset))

	'''
	notice that as 0 is included in the set, elements of set must be in the multiset.
	So, our search space has reduced to the multiset.

	Generate a set of unique values from multiset
	'''

	ms = set(multiset)
	for i in ms:

		if sum([(abs(i - j) in multiset) for j in X])  == len(X):

			for j in X:
				multiset.remove(abs(i-j))

			X.append(i)

	res = set(X)
	return sorted(res)


# Sample output


print(generate_set([2, 2, 3, 3, 4, 5, 6, 7, 8, 10]))

'''
prints as follows:

[0, 2, 4, 7, 10]

'''

