######################################################################
# FILE: balanced_brackets.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex6 2014-2015
# DESCRIPTION:
# functions for testing strings for balanced brackets
#######################################################################
def is_balanced(s):
    '''
    The function check if a string is balanced (every '(' has ')' on the right
    order)

    :param s:string
    :return:True for balanced string
            False for not balanced string
    '''

    counter_open_brackets = 0 #counts how many open brackets there are
                              #currently during the test
    s_len = len(s)
    OPEN_BRACKET = '('
    CLOSE_BRACKET = ')'
    for i in range(s_len):
        if s[i] == OPEN_BRACKET:
            counter_open_brackets += 1
        elif s[i] == CLOSE_BRACKET:
            if counter_open_brackets == 0:
                #if there isn't '(' without ')' right now, the string is
                #unbalanced because there is ')' before '('
                return False
            else:
                counter_open_brackets -= 1
    if counter_open_brackets == 0:
        #the string is balanced, because every '(' has ')' on the right order
        return True
    else:
        #there are some '(' on the string that hasn't ')'
        return False

def _lema_violated_balanced(len_s, s, counter_open_brackets):
    '''
    The function checks if a string is balanced or not

    :param len_s: int, the length of the original string
    :param s: string, the current string
    :param counter_open_brackets: int, number of '(' without ')' currently on
                                  test
    :return: ("end", counter_open_brackets) if the recursion tested the whole
                original string and found no position caused the string be
                unbalanced
             (current_pos, counter_open_brackets) if the recursion found the
                position caused the string be unbalanced
    '''

    current_pos = len_s - len(s) #position on the original string checked now
    OPEN_BRACKET = '('
    CLOSE_BRACKET = ')'

    if len(s) == 0:
        #the user entered an empty string or the recursion checked until the
        #end of the string
        return ("end", counter_open_brackets)

    first_char = s[0]
    if first_char == OPEN_BRACKET:
        #found '(', add 1 to the counter
        counter_open_brackets += 1
    elif first_char == CLOSE_BRACKET:
        #found ')'
        if counter_open_brackets == 0:
            #the string is unbalanced because there is ')' without '('
            #fot it before, return the current position and the counter
            return (current_pos, counter_open_brackets)
        else:
            #reduce 1 from counter
            counter_open_brackets -= 1

    #slice the string from index 1 to end and call lema_violated_balanced
    #with the length of original string, sliced string and the counter
    s = s[1:]
    return _lema_violated_balanced(len_s, s, counter_open_brackets)


def violated_balanced(s):
    '''
    The function gets a string, and using lema_violated_balanced checks
    if the string is balanced or not

    :param s: string
    :return: -1 if the string is balanced
             len(s) if the string is unbalanced so there are some '(' without
                ')'
             troubled_pos if the string is unbalanced and the position where
                there is ')' without '(' for it before

    '''

    #troubled_pos - position where the string became unbalanced
    #counter_open_brackets = number of '(' without ')'
    troubled_pos, counter_open_brackets = _lema_violated_balanced(len(s), s, 0)
    if troubled_pos == "end":
        #lema_violated_balanced checked until the end of s and found no
        #position caused the string be unbalanced
        if counter_open_brackets == 0:
            #the string is balanced
            return -1
        else:
            #the string has some '(' without ')', the string is unbalanced
            return len(s)
    else:
        #the string is unbalanced, return the position where that happened
        return troubled_pos


def _lema_match_brackets(match, s, i, k, counter_open_brackets):
    '''
    The function find the closing bracket of the open one of position
    i on the original string from match_brackets and p

    :param match: list of matches of '(' and ')'
    :param s: string, current string
    :param i: position of '(' that we want to find its ')'
    :param k: position on s from first call to the function
    :param counter_open_brackets: number of '(' without ')' currently

    '''

    OPEN_BRACKET = '('
    CLOSE_BRACKET = ')'

    first_char = s[0]

    if first_char == OPEN_BRACKET:
        #found '(' add 1 to counter
        counter_open_brackets += 1
    elif first_char == CLOSE_BRACKET:
        #found ')'
        if counter_open_brackets != 0:
            #there are some '(' before, reduce 1 from counter
            counter_open_brackets -= 1
        else:
            #we found the ')' of the '(' from original string
            j = i + k + 1 #j is the position of the ')' found on the original
                          #string
            match[i] = j - i
            match[j] = i - j
            return None #To stop the recursion

    k += 1 #move to next char
    s = s[1:]
    _lema_match_brackets(match, s, i, k, counter_open_brackets)


def match_brackets(s):
    '''
    The function finds couple of open and close brackets using
    _lem_match_brackets

    :param s: string
    :return: match: list of matches of each '(' and ')'
    '''

    OPEN_BRACKET = '('
    s_len = len(s)

    if(violated_balanced(s) != -1):
        #if the string is not balanced
        return []

    match =[0]*s_len #list of matches

    for i in range(s_len):
        if s[i] == OPEN_BRACKET:
            #if we find '(', we want to find its couple, so make a copy of
            #s from one char after the '(' to end and send it to
            #_lema_match_brackets to find its couple
            s_copy = s[i+1:]
            _lema_match_brackets(match, s_copy, i, 0, 0)

    return match