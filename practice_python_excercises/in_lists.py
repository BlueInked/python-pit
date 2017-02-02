import random
import operator


def random_list1():
    ''' number -> list

    Returns a random list of numbers in a given range

    '''
    
    items_in_list1 = input("Give me the number of items you want in your list:")
    stop_num1 = input("Give me the highest random number you would like:")

    my_random1 = []


    for i in range(int(items_in_list1)):

        my_random1.append(random.randrange(1, int(stop_num1),1))
    

    print (my_random1)

    
def random_list2():
    ''' number -> list

    Returns a random list of numbers in a given range

    '''

    items_in_list2 = input("Give me the another number of items you want in your list:")
    stop_num2 = input("Give me the another highest random number you would like:")

    my_random2 = []


    for i in range(int(items_in_list2)):

        my_random2.append(random.randrange(1, int(stop_num2),1))
        

    print (my_random2)



    
def overlap(random1, random2):
    ''' list -> list 

    Returns a new list of number if any included in two lists


    '''
    
    all_together = operator.add(random1, random2)
    
    in_order = sorted(all_together, key = int)

    in_both = list(set(in_order))

    print(in_both)
       




