
def main():
    word = input('camelCase: ')
    make_snake(word)


def make_snake(string):
    new_string = ''
    for letter in string:
        if letter.isupper():
            #print(f"found an upper case {letter}")
            letter = '_' + letter.lower()
        new_string = new_string + letter
    print(new_string)


if __name__ == '__main__':
    main()