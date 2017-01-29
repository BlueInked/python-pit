def divisible():
    ''' (number) -> string

    Return whether a given number divisble by another number.

    >>> num = 200, check = 5
    "Yes, 200 is divisible by 5 and equals 40."
    >>> num = 20 check = 3
    "No, 20 is not divisible by 3.
    '''
    
    num = input("Give me a number:")
    check = input("Now give me anoher number:")
    
    
    if int(num) % int(check) == 0:
        print ("Yes, " + num + " is divisible by " + check + " and equals " + str((int(num) // int(check))) + ".")
    else:
        print ("No, " + num + " is not divisible by " + check + ".")      
    

