from trie import Trie
from sentences_collection import SentencesCollection


class Completion:
    def __init__(self):
        self.trie = Trie.getInstance()
        self.sentences_collection = SentencesCollection()
        self.prev_sentences = None

    def search_completions(self, text):
        if text == '#':
            self.prev_sentences = None
            return
        sentences_id = self.trie.search(text)
        if self.prev_sentences is None:
            sentences = self.get_five_sentences(sentences_id)
        else:
            sentences_id = self.get_relevant_sentences(sentences_id)
            sentences = self.get_five_sentences(sentences_id)
        # completed_sentences=[]
        # for i in range(5):
        #     sen_obj=self.sentences_collection.get_sentence_obj(str(sentences_id[i]))
        #     completed_sentences.append(sen_obj.get_sentence())
        #     if i==len(sentences_id)-1:
        #         break
        # res=[]
        # [res.append(x) for x in completed_sentences if x not in res]
        # return res
        self.prev_sentences = sentences_id
        return sentences

    # Extract five objects of sentences by id from the fit sentences id list.
    def get_five_sentences(self, sentences_id):
        if len(sentences_id) == 0:
            return "not found"
        completed_sentences = []
        for i in range(5):
            sen_obj = self.sentences_collection.get_sentence_obj(str(sentences_id[i]))
            completed_sentences.append(sen_obj.get_sentence())
            if i == len(sentences_id) - 1:
                break
        res = []
        [res.append(x) for x in completed_sentences if x not in res]
        return res

    # Find the intersection of the previous fit sentences and the current.
    def get_relevant_sentences(self, sentences_id):
        sen_ids = [id for id in sentences_id if id in self.prev_sentences]
        return sen_ids