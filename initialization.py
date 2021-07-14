import os
import string
from queue import Queue
import re

from sentence import Sentence
from sentences_collection import SentencesCollection


class Initialization:
    def __init__(self, path):
        self.path=path
        self.sentences_collection=SentencesCollection()

    #Open the main directory, read it's sub files and directories and send the files for treatment.
    def initialize(self):
        directories=Queue()
        directories.put(self.path)
        x=''
        try:
            directory_path=''
            while not directories.empty():
                directory_path=directories.get()+'/'
                print("directory path: ",directory_path)
                for x in os.listdir(directory_path):
                    path=directory_path+x
                    print(x, os.path.isdir(path))
                    if os.path.isdir(path):
                        directories.put(path)
                    elif x.endswith(".txt"):
                        # print(directory_path,type(x))
                        # print(x,type(directory_path))
                        # path=directory_path+x
                        # print(path)
                        self.file_handler(path)
                    else:
                        raise IsADirectoryError
        except IsADirectoryError:
            print(f'Unknown file {x}')

#Read a file and send each sentence to be insert to a trie.
    def file_handler(self, file_path):
        try:
            with open(file_path, encoding="utf8") as file:
                line_number=1
                for line in file:
                    if line!="":
                        line = ''.join(x for x in line if x.isalpha() or x.isspace())
                        line = ' '.join(line.split())
                        location=file_path+str(line_number)
                        sentence=Sentence(line.rstrip(),location)
                        # print("****"+line.rstrip(),"****"+location)
                        self.sentences_collection.add_sentence_obj(sentence)
        except Exception as e:
            print(e)

