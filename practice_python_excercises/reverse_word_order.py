def reverse_reverse(forward_str):
    '''
    string -> string

    Given a string and returns the reverse of that string

    >>>reverse_reverse("The Cat in the Hat Comes Back")
    "Back Comes Hat the in Cat The"
    >>>reverse_reverse("Do or Do Not there is No Try")
    "Try No is there Not Do or Do"
    >>>reverse_reverse("We Want That Which We Should Not Want")
    "Want Not Should We Which That Want We"

    '''
  
    print(' '.join(forward_str.split()[::-1]))
    
        


            
   
