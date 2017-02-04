
def palindrome(word):
    ''' string -> boolean

    Returns whether a given word is a palindrome or not


    >>>palindrome("no")
    False
    >>>palindrome("mom")
    True
    >>>palindrome("racecar")
    True
    '''
    
    reverse = word[::-1]

    if word == reverse:
        print(True)
    else:
        print(False)



