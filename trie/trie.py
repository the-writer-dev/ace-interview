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

    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        self.output = []

        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, x[:-1])
        return sorted(self.output, key=lambda x: x[1], reverse=True)

t = Trie()
t.insert('was')
t.insert('war')
t.insert('word')
t.insert('where')
t.insert('where')
t.insert('what')

print(t.query('wh'))
print(t.query('wht'))



