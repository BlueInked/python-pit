'''
Write a function that takes an ordered list of numbers(a list where the
elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the
list and returns (then prints) an appropriate boolean.
 
 '''

def binary_search(ordered_lst, another_num):
    '''
    list, num - > boolean

    Given an ordered list and an integer returns a boolean of whether the number
    is inside the list.

    >>>binary_search([3,6,8,9,34], 5)
    False
    >>>binary_search([1,4,6,7,8], 4)
    True
    '''

    min_num = ordered_lst[0]
    max_num = ordered_lst[-1]
    m = len(ordered_lst) // 2
    mid_num = ordered_lst[m]

    #If the number is either the lowest or highest number it's automatically true
    if another_num == min_num or another_num == max_num:
        print(True)
    #If the number is greater than the highest of lower than the lowest automatically false
    if another_num < min_num or another_num > max_num:
        print(False)
    #Now to start shrinking the array
    #Since the array is in order then the number would be more than the littlest and less then the biggest
    if another_num > min_num and another_num < max_num:
        while another_num != mid_num:
            if another_num > mid_num:
                min_num = mid_num
            if another_num < mid_num:
                max_num = mid_num
   
        

        
        
        



