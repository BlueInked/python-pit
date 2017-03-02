'''
Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping. One .txt file has a list of all prime
numbers under 1000, and the other .txt file has a list of happy numbers up
to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other
number. And yes, happy numbers are a real thing in mathematics - you can look
it up on Wikipedia. The explanation is easier with an example, which I will
describe below.)
'''

def overlapping():
    '''
    Returns a list of overlapping iems from two txt files.
    
    '''

primeslist = []
with open('primenumbers.txt') as primesfile:
	line = primesfile.readline()
	while line:
		primeslist.append(int(line))
		line = primesfile.readline()

happieslist = []
with open('happynumbers.txt') as happiesfile:
	line = happiesfile.readline()
	while line:
		happieslist.append(int(line))
		line = happiesfile.readline()

overlaplist = []
for elem in primeslist:
	if elem in happieslist:
		overlaplist.append(elem)
		
print(overlaplist)
