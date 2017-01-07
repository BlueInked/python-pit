import re

print("Welcome to the Python Calculator")
print("To stop calculator type: quit")

previous = 0
run = True

def perform_math():
    '''(numbers) -> numbers

    accepts numbers from the user and performs continuous
    mathematical equations on them.

    precondition input must be numbers and mathematical signs
    
    '''
    
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Type in an Equation:")
    else:
        equation = input(str(previous))
        
    #Is it too much to want to figure out a way to "force" numerical input?
        
    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,:()" "]', '' , equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
            

while run:
    perform_math()
