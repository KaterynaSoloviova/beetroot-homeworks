# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
# and the number of occurrences as values.

str = input('Enter a sentence: ')

def new_dictionary_v1(str):
    result = {}
    word = ""
    str = str + " "
    for i in range(len(str)):
        if str[i] != " ":
            word = word + str[i]
        else:
            if word == '':
                continue
            if word not in result:
                result[word] = 1
            else:
                result[word] = result[word] + 1
            word = ""
    return result

print(new_dictionary_v1(str))

def new_dictionary_v2(str):
    result = {}
    word = ""
    words = str.split(" ")
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] = result[word] + 1

    return result

print(new_dictionary_v2(str))
