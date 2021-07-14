class SentencesCollection:
    __instance=None
    __sen_counter=0

    def __new__(cls, *args, **kwargs):
        if not SentencesCollection.__instance:
            SentencesCollection.__instance = object.__new__(cls)
        return SentencesCollection.__instance

    def __init__(self):
        self.sentences_collection={}

    def add_sentence(self, sentence_object):
        SentencesCollection.__sen_counter+=1
        self.sentences_collection[SentencesCollection.__sen_counter]=sentence_object

    def get_sentence(self, id):
        return self.sentences_collection[id]

    def get_sentences_collection(self):
        return self.sentences_collection
