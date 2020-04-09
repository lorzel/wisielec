sentence_main = 'reguły są po to, aby je łamać'
letters_list = []
list = []
list2 = []
dict_list = []
alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z', 'ż', 'ź']

dictionary = {}
dictionary2 = {}


def sentence_to_letters(sentence):
    for word in sentence:
        for letter in word:
            letters_list.append(letter)


def generate_stars(words):
    i = 0
    for word in words:
        for letter in word:
            if letter.lower() in alphabet:
                dictionary2 = {i: '*'}
                dictionary.update(dictionary2)
                i += 1
                list.append('*')
            else:
                dictionary2 = {i: letter}
                dictionary.update(dictionary2)
                i += 1
                list.append(letter)
            star_sentence = ''.join(list)
    #print(star_sentence)


def update_stars(sentence, char):
    i = 0
    for word in sentence:
        for letter in word:
            if letter == char and letter in letters_list:
                dictionary2 = {i: letter}
                dictionary.update(dictionary2)
                i += 1

            elif dictionary[i] != '*':
                dictionary2 = {i: letter}
                dictionary.update(dictionary2)
                i += 1

            elif letter in alphabet:
                dictionary2 = {i: '*'}
                dictionary.update(dictionary2)
                i += 1

            else:
                dictionary2 = {i: letter}
                dictionary.update(dictionary2)
                i += 1
    dict_to_string(dictionary)


def dict_to_string(dict):
    for x in dict.values():
        dict_list.append(x)
    print("".join(dict_list))
    dict_list.clear()



sentence_to_letters(sentence_main)
generate_stars(sentence_main)

update_stars(sentence_main, '')
user_input = input('Litera: ')
update_stars(sentence_main, user_input)
user_input2 = input('Litera: ')
update_stars(sentence_main, user_input2)
