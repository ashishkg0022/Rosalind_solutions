class Trie:
    
    def __init__(self, dna=None):
        self.count = 1
        self.root = [self.count,{}]

        if isinstance(dna, list):
            for i in dna:
                self.insert(i)
        elif isinstance(dna, str):
            self.insert(dna)

    def insert(self, dna):
        node = self.root
        for char in dna:
            if not char in node[1]:
                self.count += 1
                node[1][char] = [self.count,{}]
            node = node[1][char]

    def print_adjacency_list(self, root = None):
        
        if root == None:
            root = self.root
        
        for char, node in root[1].items():
            print(root[0], node[0], char)
            self.print_adjacency_list(node)



# Sample output (Note: Order of printing may vary, but all nodes are printed)

T = Trie(['ATAGA','ATC','GAT'])
T.print_adjacency_list()

'''
Or,  it can also be wriiten as

>>> T = Trie()
>>> T.insert('ATAGA')
>>> T.insert('ATC')
>>> T.insert('GAT')
>>> T.print_adjacency_list()
'''