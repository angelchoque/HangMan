import os
import random


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")


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
    random_word = random.randrange(len(data))
    word = data[random_word]
    word = word.upper()
    for i in word:
        list_word.append(i)
    list_word.pop()
    return list_word


def letter_analitic(letter):
    if len(letter) > 1:
        print('----- Solo puedes ingresar un caracter -----')


def condition(word):
    lines = []
    index_lines = []
    word_correct = ''.join(word)
    print(word)
    index_word = list(enumerate(word))
    for i in word:
        lines.append('-')
        index_lines.append('-')
    lines = ''.join(lines)
    print(lines)
    hearts = 12
    a = 0
    while(a<hearts):
        print('Tienes ' + str(hearts-a) + ' vidas')
        letter = input('Ingresa una letra: ')
        letter = normalize(letter)
        letter = letter.upper()
        letter_analitic(letter)
        for x in range(len(index_word)):
            var = index_word[x][1]
            var = normalize(var)
            if letter == var:
                index_lines[x] = index_lines[x].replace('-',letter)
            var = ''.join(index_lines)
        lines = var            
        print(lines)
        if lines == word_correct:
            print('WINNN')
            break
        a=a+1
        

def run():
    word = read_text()
    condition(word)


if __name__ == '__main__':
    run()