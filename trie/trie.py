# trie operations
# 1. insert a word into a trie
# 2. searching for words using a prefix

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        # count how many times a word was inserted
        self.counter = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        n = self.root

        for char in word:
            if char in n.children:
                n = n.children[char]
            else:
                node = TrieNode(char)
                n.children[char] = node
                n = node
        n.is_end = True
        n.counter += 1

    def dfs(self, n, prefix):
        if n.is_end:
            self.output.append((prefix + n.char, n.counter))

        for child in n.children.values():
            self.dfs(child, prefix + n.char)

    def query(self, x):
        self.output = []

        n = self.root
        for char in x:
            if char in n.children:
                n = n.children[char]
            else:
                return []
        
        # currently n = 'w' -> 'h'
        # prefix should be 'w'
        self.dfs(n, x[:-1]) 
        return sorted(self.output, key=lambda x: x[1], reverse=True)
# 
#          w
#       /  |  \ 
#      a   o   h 
#     / \  |   | \
#    s   r r   a  e
#          |   |   \
#          d   t    r
#                    \
#                     e

t = Trie()
t.insert('was')
t.insert('war')
t.insert('word')
t.insert('where')
t.insert('where')
t.insert('what')

print(t.query('wh'))
print(t.query('wht'))



