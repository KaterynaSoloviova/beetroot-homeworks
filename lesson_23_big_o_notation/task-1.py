from typing import List, Tuple


# We assume that all lists passed to functions are same length N


# answers
# 1 - n
# 2 - 1
# 3 - n^2
# 4 - n
# 5 - n^2
# 6 - log n


# Question 1: O(1) + O(n)*(O(n) + O(1)) = O(1) + O(n^2) + O(n) = O(n^2)
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []  # O(1)
    for el_first_list in first_list:  # O(n)
        if el_first_list in second_list:  # O(n)
            res.append(el_first_list)  # O(1)
    return res


# Question 2: O(10)
def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


# Question 3: O(n) + O(n)*(O(n) + O(n))= O(n + n(2n)) = O(n + 2n^2) = O(n^2)
def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]  # O(n)
    for el_second_list in second_list:  # O(n)
        flag = False
        for check in temp:  # O(n)
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)  # O(1) on average or O(n) in worst-case
    return temp

# Question 3: O(1) + O(n)*(O(1) + O(1))= O(1 + 2n) = O(n)
def question4(input_list: List[int]) -> int:
    res: int = 0  # O(1)
    for el in input_list:  # O(n)
        if el > res:  # O(1)
            res = el  # O(1)
    return res
