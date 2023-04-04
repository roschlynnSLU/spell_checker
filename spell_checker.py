from words import Words


english_words = Words('english.txt')
sentence = input('Enter a sentence: ')
word_list = sentence.split(' ')
for word in word_list:
    if not english_words.is_word(word.strip()):
        print('correcting', word)
        corrections = english_words.get_replace_corrections(word)
        print('Replace suggestions: ', corrections)
        corrections = english_words.get_delete_corrections(word)
        print('Delete suggestions: ', corrections)
        corrections = english_words.get_add_corrections(word)
        print('Add suggestions: ', corrections)
