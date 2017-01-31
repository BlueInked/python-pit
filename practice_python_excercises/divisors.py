

    
def divisor():
    ''' numbers -> list of numbers

    Returns a list of all the numbers that are divisors of a given number

    >>> 25
    [1,5]
    >>> 100
    [1,2,4,5,10,20,25,50]
    '''
    
    div = []
    number = input("Give me a number, any number:")
    for num in range(1, int(number)):
        if int(number) % int(num) == 0:
            div.append(num)
            
    print(div)
        


