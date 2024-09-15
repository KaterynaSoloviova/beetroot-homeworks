# Determine the complexity of one of the existing tasks (task-1 from lesson_07) .

from collections import defaultdict

str = input('Enter a sentence: ')


# O(n^2)
def new_dictionary_v1(str):
    result = {}  # O(1)
    word = ""  # O(1)
    str = str + " "  # O(1)
    for i in range(len(str)):  # O(n)
        if str[i] != " ":  # O(1)
            word = word + str[i]  # O(n)
        else:
            if word == '':  # O(1)
                continue
            if word not in result:  # O(n)
                result[word] = 1  # O(1)
            else:
                result[word] = result[word] + 1  # O(1)
            word = ""  # O(1)
    return result


print(new_dictionary_v1(str))   # O(1)


# O(n) on average or O(n^2) in the worst case
def new_dictionary_v2(str):
    result = {}  # O(1)
    word = ""  # O(1)
    words = str.split(" ")  # O(n) where n is the length of the string
    for word in words:  # O(n)
        if word not in result:  # O(1) on average or O(n) in the worst case
            result[word] = 1  # O(1)
        else:
            result[word] = result[word] + 1  # O(1)

    return result


print(new_dictionary_v2(str))  # O(1)


# O(n)
def new_dictionary_v3(str):
    result = defaultdict(int)  # O(1)
    words = str.split(" ")  # O(n)
    for word in words:  # O(n)
        result[word] += 1  # O(1)

    return result


print(new_dictionary_v3(str))  # O(1)
