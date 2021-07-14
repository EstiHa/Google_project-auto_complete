import os
from queue import Queue

class Initialization:
    def __init__(self, path):
        self.path=path

    def initialize(self):
        directories=Queue()
        # directories.put()
        directory_path=self.path
        for x in os.listdir(directory_path):
            pass