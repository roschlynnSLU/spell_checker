from words import Words


english_words = Words('english.txt')
sentence = input('Enter a sentence: ')
word_list = sentence.split(' ')
for word in word_list:
    if not english_words.is_word(word.strip()):
        print('correcting', word)