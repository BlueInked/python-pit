'''
Write a function that takes an ordered list of numbers(a list where the
elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the
list and returns (then prints) an appropriate boolean.
 
 '''

def search(ordered_lst, another_num):
    '''
    list, num - > boolean

    Given an ordered list and an integer returns a boolean of whether the number
    is inside the list.

    >>>search([3,6,8,9,34], 5)
    False
    >>>search([1,4,6,7,8], 4)
    True
    '''

    if another_num in ordered_lst:
        return True
    return False




