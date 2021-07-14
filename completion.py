from trie import Trie
from sentences_collection import SentencesCollection

class Completion:
    def __init__(self):
        self.trie=Trie.getInstance()
        self.sentences_collection=SentencesCollection()

    def search_completions(self, text):
        sentences_id=self.trie.search(text)
        print(sentences_id)
        completed_sentences=[]
        for i in range(5):
            sen_obj=self.sentences_collection.get_sentence_obj(str(sentences_id[i]))
            completed_sentences.append(sen_obj.get_sentence())
            if i==len(sentences_id)-1:
                break
        print(completed_sentences)
        return completed_sentences