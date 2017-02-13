import random
import string

def password():
    '''
    int -> string

    Given a requested password length gives back a randomly populated string

    '''
  
    pass_len = int(input("How long would you like your password to be?:"))
    
    return ''.join(random.sample((string.ascii_uppercase + string.digits + string.ascii_lowercase),(pass_len)))
            
   
