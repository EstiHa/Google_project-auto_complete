class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = []


class Trie():
    def __init__(self):

        self.root = TrieNode()

    def insert(self, string,id_of_sen):
        node = self.root
        for a in list(string):
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        node.last.append(id_of_sen)
    def search(self, key):
        node = self.root
        found = True
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        if found and node:
            return node.last
        else:
            return False

    def print_trie(self,node=None,word=''):
        if not node:
            node=self.root
        else:
            print(word+':')
            for item in node.last:
                print(item,end=" ")
            print('\n')

        for a, n in node.children.items():
            self.print_trie(n, word + a)


# creating trie object
t = Trie()
t.insert("lk",4)
t.insert("la",3)
t.insert('l',2)
t.insert('l',1)
print(t.search('l'))
t.print_trie()

