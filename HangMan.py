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
    for i in word:
        list_word.append(i)
    list_word.pop()
    return list_word


def comparate(x,a,lines):
    pass


def condition(word):
    lines = []
    index_lines = []
    print(word)
    
    index_word = list(enumerate(word))
    
    for i in word:
        lines.append('-')
        index_lines.append('-')
    lines = ''.join(lines)
    print(lines)
    for i in range(5):
        letter = input('Ingresa una letra: ')
        for x in range(len(index_word)):
            if letter == index_word[x][1]:
                index_lines[x] = index_lines[x].replace('-',letter)
                # print(index_lines)
            var = ''.join(index_lines)
        lines = var            
        print(lines)
            



    """ for i in range(1):
        a = input('Ingresa una letra: ')
        print(index_word)
        for x in word:
            if a == x:
                # comparate(x,a,lines) """

                


def run():
    word = read_text()
    condition(word)
    # print('----------------------')
    # print(normalize('é'))


if __name__ == '__main__':
    run()