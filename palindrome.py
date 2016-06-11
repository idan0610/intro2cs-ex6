######################################################################
# FILE: palindrome.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex6 2014-2015
# DESCRIPTION:
# functions for testing palindromes
#######################################################################
def is_palindrome_1(s):
    '''
    The function check if a string is palindrome or not

    :param s: string for checking
    :return: True if s is a palindrome, False for s is not a palindrome
    '''
    len_s = len(s)
    if len_s > 1:
        #if the length of s larger then 1, means the check not finished until
        #the middle of s
        first_char = s[0]
        last_char = s[len_s - 1]
        if first_char != last_char:
            #s is not a palindrome
            return False
        else:
            #create new string from index 2 to len(s) - 1
            new_s = s[1:len_s-1]
            return is_palindrome_1(new_s)

    #if the check is finished, means the check got to the middle of s,
    #the length of s is 0 or 1, so return True
    return True

def is_palindrome_2(s, i, j):
    '''
    The function check if a sub-string of string from index i to j is
    a palindrome or not

    :param s: string for checking
    :param i: index of first char
    :param j: index of last char
    :return: True if the string from s[i] to s[j] is a palindrome,
             False if the string from s[i] to s[j] is not a palindrome
    '''
    if len(s) != 0:
        #Only if the string is not empty, place the first and last chars
        #in variables
        first_char = s[i]
        last_char = s[j]

    if len(s) == 0 or i == j or (i + 1 == j and first_char == last_char):
        #if the string is empty, there is only 1 char,
        #or last 2 chars and they are the same
        return True
    elif i > j or first_char != last_char:
        #if the user entered i larger then j, or first_char and last_char
        #are not the same
        return False
    return is_palindrome_2(s, i+1, j-1)