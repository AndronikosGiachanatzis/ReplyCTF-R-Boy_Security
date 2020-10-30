

def getdict(filename):
    '''
    Groups the words of the file in a dictionary by word length
    :param filename: the name of the file
    :return: the dictionary grouped by length of words
    '''
    ldict = {}
    with open(filename, "r") as f:
        for line in f:
            if len(line)-1 not in ldict.keys():
                ldict[len(line)-1] = []
            ldict[len(line)-1].append(line[:-1])
    return ldict




def encrypt_string(hash_string):
    '''
    Encrypts a string with SHA-256
    :param hash_string: the string to be encrypted
    :return: the hash digest
    '''
    import hashlib

    return hashlib.sha256(hash_string.encode()).hexdigest()


def listToString(list):
    '''
    Converts a list to string format
    :param list: the list to be converted
    :return: a string representation of the list
    '''
    string = ''
    for i in list:
        string += (''.join(i))
    return string


def generateoutputlist(name):
    '''
    Puts the words of a file in a list in the same order as in the file
    :param name: the name of the file
    :return: the list containing the ordered words
    '''
    list = []
    with open(name) as f:
        for word in f:
            list.append(word.replace('\n', ''))
    return list


def descramble(odict, scramble_filename):
    '''
    Descrambles the scrambled word lists
    :param odict: the dictionary containing the normal words
    :param scramble_filename: the name of the file of the scrambled words
    :return: the unscrambled words to which every scrambled word corresponds
    '''

    slist = generateoutputlist(scramble_filename)
    print(len(slist))
    # the list containing the unscrambled word list
    sol_list = []

    # for every word in the scrambled word list find to which unscrambled word it corresponds
    for sword in slist:
        dlist = odict[len(sword)]

        for dword in dlist:
            # continue until you find a character that is not in dword
            next_word = False
            for i in sword:
                if i not in dword:
                    next_word = True
            # if all the characters of a scrambled word are in a normal word and it is indeed the same word add it to the sol_list
            if not next_word and sorted(dword) == sorted(sword):
                sol_list.append(dword)

    return sol_list


def main():
    # get the dictionary of the original words grouped by length
    dict_filename = 'dictionary.txt'
    odict = getdict(dict_filename)

    scramble_filename = 'scrambled-words.txt'

    # descramble the words
    sol_list = descramble(odict, scramble_filename)
    sol_string = listToString(sol_list)
    # encrypt the string that leads to the flag
    flag = encrypt_string(sol_string)

    # write the flag to the solution file
    with open('flag.txt', 'w') as f:
        f.write("{FLG:" + flag + "}")


if __name__ == '__main__':
    main()
