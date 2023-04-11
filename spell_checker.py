from words import Words #Import the py file

english_words = Words('english.txt') #Pass the txt file to the class
sentence = input('Enter a sentence: ') #Enter the sentence to be checked
word_list = sentence.split(' ') #Split the sentence into individual words
for word in word_list: #Loop through every word
    if not english_words.is_word(word.strip()): #Check if the word is present in the file or not
        print('correcting', word) #Begin correcting the word
        corrections = english_words.get_replace_corrections(word) #First get the word suggetions that can be replaced
        print('Replace suggestions: ', corrections) #Show the replace suggestions to the user
        corrections = english_words.get_delete_corrections(word) #Then get suggestions that can be shown by deletion
        print('Delete suggestions: ', corrections)
        corrections = english_words.get_add_corrections(word) #Then get suggestions that can be added by addition of words
        print('Add suggestions: ', corrections)
