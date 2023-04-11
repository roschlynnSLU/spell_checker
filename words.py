class Words:
    def __init__(self, file_name): #Constructor takes file name as argument
        self.words = [] #Define list
        with open(file_name) as word_dictionary: #Open the file for reading
            for word in word_dictionary: #Read until file ends
                self.words.append(word.strip('\n')) #Remove trailing white spaces and append to the list
    
    def is_word(self, word): #Check whether word is present in the list or not
        return word in self.words #Returns true or false depending on whether the words are present in the list or not

    def get_size(self): #Get the size of the word
        return len(self.words) #Returns the size of the word

    def get_replace_corrections(self, misspelled_word): #Returns the potential list of corrections for the word
        suggestions = [] #Creates a list to store the suggestions
        for w in self.words: #Loop through all the words found from the file
            # only consider words that have the same length as misspelled_word
            if len(w) == len(misspelled_word):
                # try replacing one letter at a time and see if we can transform the misspelled word into word w
                for index in range(0, len(w)): #Loop through every position of the word
                    correction = misspelled_word[0:index]+w[index] #Construct a new string called correction by replacing the letter at that position
                    if index < len(w)-1: #Check if the index is less than the length of the word
                        correction+=misspelled_word[index+1:] #Correction transformation
                    # test if replaced letter transforms our word to w    
                    if correction == w: #If transformed word matches the word
                        suggestions.append(w) #Append the transformed word to suggestions list and exit the loop
                        break
        return suggestions #Return the suggested words
        
    def get_delete_corrections(self, misspelled_word): #Check if transformation is possible by deletion
        suggestions = [] #Initialize suggestions list
        for w in self.words: #Loop through the words
            # only consider words that are one character shorter than misspelled_word
            if len(w) == len(misspelled_word)-1:
                # try deleting one character from misspelled word at a time and see if it transforms to word w
                if self.can_ransform_with_delete(misspelled_word, w):
                    suggestions.append(w)
        return suggestions
    
    def get_add_corrections(self, misspelled_word):
        suggestions = []
        for w in self.words:
            # only consider words that are one character longer than misspelled word
            if len(w) == len(misspelled_word)+1:
                if self.can_ransform_with_delete(w, misspelled_word):
                    suggestions.append(w)
        return suggestions

    def can_ransform_with_delete(self, source, dest): #Check whether source and destionation word match
        transformed = False #Assume false by default
        for index in range(0, len(source)): #Loop through every letter of the word
            correction = source[0:index] #Create a new correction string from 0 to the end of the character string
            if index < len(source)-1: #Append the string from the omitted letter till the end
                correction+=source[index+1:]
            # test if deleted letter transforms our word to w
            if correction == dest: #Check if the transofrmed letter is equal to the destination then set to true
                transformed = True
                break
        return transformed #Return the transformed word