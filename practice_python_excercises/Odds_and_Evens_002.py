

    
def odd_or_even():
    ''' (number) -> string

    Return whether a given number is even or odd.

    >>> 16
    "16, is an even number."
    >>> 161
    "161, is an odd number."
    '''
    
    number = input("Give me a number:")

    if int(number) % 2 == 0:
        print (number + ", is an even number.")
    else:
        print (number + ", is an odd number.")
        


