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

    def get_replace_corrections(self, misspelled_word):
        suggestions = []
        for w in self.words:
            # only consider words that have the same length as misspelled_word
            if len(w) == len(misspelled_word):
                # try replacing one letter at a time and see if we can transform the misspelled word into word w
                for index in range(0, len(w)):
                    correction = misspelled_word[0:index]+w[index]
                    if index < len(w)-1:
                        correction+=misspelled_word[index+1:]
                    # test if replaced letter transforms our word to w    
                    if correction == w:
                        suggestions.append(w)
                        break
        return suggestions
        
    def get_delete_corrections(self, misspelled_word):
        suggestions = []
        for w in self.words:
            # only consider words that are one character shorter than misspelled_word
            if len(w) == len(misspelled_word)-1:
                # try deleting one character from misspelled word at a time and see if it transforms to word w
                for index in range(0, len(w)):
                    correction = misspelled_word[0:index]
                    if index < len(w)-1:
                        correction+=misspelled_word[index+1:]
                    # test if deleted letter transforms our word to w
                    if correction == w:
                        suggestions.append(w)
                        break
        return suggestions
    
    def get_add_corrections(self, misspelled_word):
        suggestions = []
        for w in self.words:
            # only consider words that are one character longer than misspelled word
            if len(w) == len(misspelled_word)+1:
                for index in range(0, len(w)):
                    if w[0:index] == misspelled_word[0:index] and w[index+1:] == misspelled_word[index:]:
                        suggestions.append(w)
                        break
        return suggestions