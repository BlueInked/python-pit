

    
def to_one_hundred():
    ''' (string and number) -> string

    Return given name and age in a string that tells the person what year they will be 100.

    >>> to_one_hundred(Steve, 90)
    "Steve, you will be 100 in 2027.
    >>> to_one_hundred(Alice, 25)
    "Alice, you will 100 in 2092.
    '''
    
    name = input("What is Your name?:")
    age = input("How old are you?:")

    print (name + ", you will be 100 in " + str(100 - int(age) + 2017))
