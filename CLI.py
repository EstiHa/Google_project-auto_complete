# class CLI:
#
#     while True:
#         print("Enter your text:")
#         text=input()
from initialization import Initialization
from trie import Trie

if __name__ == '__main__':
    initialize=Initialization('pages')
    initialize.initialize()
    mt=Trie.getInstance()
    mt.print_trie()
    print(mt.search("hey"))
