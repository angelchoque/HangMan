import os
import random


def normalize(s): # It removes the accents of a string
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s


def read_text(): 
    data = []
    list_word = []
    with open('./files/data.txt','r',encoding='utf-8') as f:
        for word in f:
            data.append(word)
    word = data[random.randrange(len(data))].upper()
    for i in word:
        list_word.append(i)
    list_word.pop()
    return list_word


def condition(word):
    lines = []
    index_lines = []
    hearts = 12
    word_correct = ''.join(word)
    # index_word = word
    for i in word:
        lines.append('-')
        index_lines.append('-')
    lines = ''.join(lines)
    for a in range(hearts):
        print(word)
        print('Tienes ' + str(hearts-a) + ' vidas')
        print('>>> '+lines)
        letter = input('Ingresa una letra: ')
        letter = normalize(letter).upper()
        for x in range(len(word)):
            # var = index_word[x]
            var = normalize(word[x])
            if letter == var:
                index_lines[x] = index_lines[x].replace('-',letter)
            var = ''.join(index_lines)
        lines = var
        if lines == word_correct:
            print('WINNN')
            break
        os.system('cls')


def run():
    word = read_text()
    condition(word)


if __name__ == '__main__':
    run()