######################################################################
# FILE: y_tree.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex6 2014-2015
# DESCRIPTION:
# Drawing a Y tree
#######################################################################
import turtle
DEFAULT_LENGTH = 200
def draw_tree(length=DEFAULT_LENGTH):
    '''
    The function draws a Y tree with Y sub-trees with each line has the
    length of the line on previous tree * 0.6

    :param length: int, length of first line to draw

    '''
    LIMIT_LINE = 10
    ANGLE = 30
    FACTOR = 0.6
    if length >= LIMIT_LINE:
        #when length under the limit, the recursion will stop
        turtle.forward(length)
        turtle.left(ANGLE)
        draw_tree(FACTOR*length) #draw the next tree with length of line * 0.6
        turtle.right(2*ANGLE) #move 60 degrees right to draw the second line
                              #of tree
        draw_tree(FACTOR*length)
        turtle.left(ANGLE)
        turtle.backward(length) #return to start of tree