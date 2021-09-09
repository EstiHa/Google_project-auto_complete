from completion import Completion
from initialization import Initialization


class CLI:
    def __init__(self, completion):
        self.completion = completion

    def run(self):
        while True:
            prev_sentence = self.completion.get_prev_sentence()
            if prev_sentence is None:
                print("Enter your text:")
                prev_sentence=''
            else:
                print(prev_sentence, end='')
            text = input()

            # text = prev_sentence + input()
            sentences = self.completion.search_completions(text)
            if sentences == "not found":
                print("The sentence was not found")
            elif sentences is not None:
                # sentences.sort()
                for i in range(len(sentences)):
                    print(
                        f'{i + 1}. {sentences[i].get_sentence()} ({sentences[i].get_location()},{sentences[i].get_sentence_index()})')


if __name__ == '__main__':
    initialize = Initialization('2021_archive')
    initialize.initialize()

    completion = Completion()
    CLI = CLI(completion)
    CLI.run()
