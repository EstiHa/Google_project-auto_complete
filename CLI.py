from completion import Completion
from initialization import Initialization
# from trie import Trie

class CLI:
    def __init__(self, completion):
        self.completion=completion

    def run(self):
        while True:
            print("Enter your text:")
            text=input()
            completion.search_completions(text)


if __name__ == '__main__':
    initialize=Initialization('pages')
    initialize.initialize()

    completion=Completion()
    CLI=CLI(completion)
    CLI.run()
    # mt=Trie.getInstance()
    # mt.print_trie()
    # print(mt.search("hey"))



