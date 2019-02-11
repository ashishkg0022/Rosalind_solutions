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
It prints:

1 8 G
8 9 A
9 10 T
1 2 A
2 3 T
3 7 C
3 4 A
4 5 G
5 6 A

=========================
Or,  Trie can also be used in the following way. Same output comes.

T = Trie()
T.insert('ATAGA')
T.insert('ATC')
T.insert('GAT')
T.print_adjacency_list()

'''