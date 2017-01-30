

    
def less_than(list1, num):
    ''' (list of numbers) -> list of numbers

    Returns numbers in a llist that are less than a given number.

    >>> less_than([3,6,79,99,102,5,10], 15)
    [3, 6, 5, 10]
    >>> less_than([100, 9, 560, 70, 75, 3,], 10)
    [9,3]
    '''
    
    less_than_list = []

    for number in list1:
        if number < num:
            less_than_list.append(number)
            
    print(less_than_list)
        


