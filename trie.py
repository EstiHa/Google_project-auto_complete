class TrieNode():

    def __init__(self):
        self.children = {}
        self.last = []


class Trie():
    __instance = None

    # def __new__(cls):
    #     if Trie.__instance is None:
    #         Trie.__instance = object.__new__(cls)
    #     return Trie.__instance
    #
    # def __init__(self):
    #     self.root = TrieNode()

    # __instance = None

    @staticmethod
    def getInstance():
        if not Trie.__instance:
            Trie()
        return Trie.__instance

    def __init__(self):
        if Trie.__instance:
            raise Exception("Trie is singleton class,"
                            " Instead of initial new Instance you"
                            " can use the getInstance() method.")
        Trie.__instance = self
        self.root = TrieNode()

    def insert(self, string,id_of_sen):
        node = self.root
        for a in list(string):
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        node.last.append(id_of_sen)

    def search(self, key):
        index_array=[]
        node = self.root
        found = True
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        if found and node:
            self.extend_sub_tree(node,index_array)
            # index_array.extend(node.last)
        return index_array


    def extend_sub_tree(self,node,sol,word=''):
        sol.extend(node.last)
        for a, n in node.children.items():
            self.extend_sub_tree(n,sol, word + a)


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
# t = Trie.getInstance()
# t.insert("lk",4)
# t.insert("la",3)
# t.insert('l',2)
# t.insert('l',1)
# print(t.search('l'))
# t.print_trie()
# t2=Trie.getInstance()
# print(t.search('l'))
# t.print_trie()


