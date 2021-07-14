from sentence import Sentence
from sentences_collection import SentencesCollection
from trie import Trie

sen1=Sentence("hy 1","page1")
sen2=Sentence("hy 2","page1")
sen3=Sentence("hy 3","page1")
sen4=Sentence("hy 4","page1")


my_sen_coll=SentencesCollection()
my_sen_coll.add_sentence_obj(sen1)
my_sen_coll.add_sentence_obj(sen2)
my_sen_coll.add_sentence_obj(sen3)
my_sen_coll.add_sentence_obj(sen4)

my_trie=Trie.getInstance()
my_trie.print_trie()
# print(my_trie.search("hy 4"))
