class Words:
    def __init__(self, file_name):
        self.words = []
        with open(file_name) as word_dictionary:
            for word in word_dictionary:
                self.words.append(word.strip('\n'))
    
    def is_word(self, word):
        return word in self.words

    def get_size(self):
        return len(self.words)
    