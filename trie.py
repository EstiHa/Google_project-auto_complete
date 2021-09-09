import config
from score import get_score

class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = []

class Trie():
    __instance = None
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

    def insert(self, string, id_of_sen):
        node = self.root
        for a in list(string):
            config.index -= 1
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
            if config.index == 0:
                break
        node.last.append(id_of_sen)

    def search(self, key):
        index_array = [{}]
        self.search_with_changes(key, index_array)
        res = []
        without_dups = set()
        for i in sorted(index_array[0].keys()):
            for item in index_array[0][i]:
                if item not in without_dups:
                    without_dups.add(item)
                    res.append(item)
        return res

    def search_exactly(self,key, node,index_array, reduce=0,  index_of_a=0):
        found = True
        for a in list(key[index_of_a:]):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        if found and node:
            if not index_array[0].get(str(reduce)):
                index_array[0][str(reduce)]=[]
            self.extend_sub_tree(node, index_array[0][str(reduce)])

    def search_with_changes(self, key, index_array):
        node = self.root
        reduce=0
        found = True
        index_of_a=-1
        for a in list(key):
            index_of_a+=1
            ######
            self.search_exactly(key, node, index_array,reduce+get_score("char_add",index_of_a), index_of_a+1)
            for k, v in node.children.items():
                self.search_exactly(key,v, index_array, reduce+get_score("char_remove",index_of_a), index_of_a)
                self.search_exactly(key, v, index_array, reduce+get_score("char_change",index_of_a), index_of_a+1)
            ######
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        if found and node:
            # print(index_array)
            index_array[0]["0"]=[]
            self.extend_sub_tree(node, index_array[0]["0"])

    def extend_sub_tree(self, node, sol, word=''):
        sol.extend(node.last)
        for a, n in node.children.items():
            self.extend_sub_tree(n, sol, word + a)

    def print_trie(self, node=None, word=''):
        if not node:
            node = self.root
        else:
            print(word + ':')
            for item in node.last:
                print(item, end=" ")
            print('\n')
        for a, n in node.children.items():
            self.print_trie(n, word + a)
