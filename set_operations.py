
class Set:

    def __init__(self, *elements):

        self.st = set(elements)
    
    def union(self, other):
        return self.st | other.st

    def intersection(self, other):
        return self.st & other.st

    def diff(self, other):
        return self.st - other.st

    def complement(self, n):
        return Set(*range(1, n+1)).st - self.st


#sample output

n = 10
A = Set(1, 2, 3, 4, 5)
B = Set(2, 8, 5, 10)

print(A.union(B))
print(A.intersection(B))
print(A.diff(B))
print(B.diff(A))
print(A.complement(n))
print(B.complement(n))

'''
prints the following:

{1, 2, 3, 4, 5, 8, 10}
{2, 5}
{1, 3, 4}
{8, 10}
{8, 9, 10, 6, 7}
{1, 3, 4, 6, 7, 9}

'''