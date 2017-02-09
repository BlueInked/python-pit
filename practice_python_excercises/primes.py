def is_a_prime():
    '''
    int -> string

    Given an integer prints whether or not that integer is a prime number.

    >>>is_a_prime(10)
    "10, is not a prime number."
    >>>is_a_prime(3)
    "3, is a prime number."
    >>>is_a_prime(107)
    "107, is a prime number."
    

    '''

    
    
    div = []
    number = input("Give me a number, any number:")
    for num in range(1, int(number)):
        if int(number) % int(num) == 0:
            div.append(num)
    if div == [1]:
        print(number + ", is a prime number.")
    else:
        print(number + ", is not a prime number.")


            
   
