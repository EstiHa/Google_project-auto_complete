import os
from queue import Queue

from sentence import Sentence


class Initialization:
    def __init__(self, path):
        self.path=path

    #open the main directory, read itws sub fies and directories and send the files for treatment.
    def initialize(self):
        directories=Queue()
        directories.put(self.path)
        x=''
        try:
            while not directories.empty():
                directory_path=directories.get()
                for x in os.listdir(directory_path):
                    if os.path.isdir(x):
                        directories.put(x)
                    elif os.path.isfile(x):
                        self.file_handler(x)
                    else:
                        raise IsADirectoryError
        except IsADirectoryError:
            print(f'Unknown file {x}')

#Read a file and send each sentence to be insert to a trie.
    def file_handler(self, file_path):
        try:
            with open(file_path) as file:
                line_number=1
                for line in file:
                    if line!="":
                        location=file_path+line_number
                        sentence=Sentence(line,location )
                        # sentences_collection.add_sentence(line)
        except Exception as e:
            print(e)

