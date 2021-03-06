'''Given any initial natural number, consider the sequence of numbers generated by repeatedly following the rule:

divide by two if the number is even or
multiply by 3 and add 1 if the number is odd.
The Collatz conjecture states that this sequence always terminates at 1. For example, the sequence generated by 23 is:

23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1

Dependency: Run on Codeskulptor

By Yuttanant Suwnansiri 11 May 2013
'''
# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

# global state

result = 23
iteration = 0
max_iterations = 16

# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n
    
def get_next(current):
    even = current % 2
    if even == 0:
       current = current / 2
    else:
       current = current * 3 + 1
    return current

# timer callback

def update():
    """???  Part of mystery computation."""
    global iteration, result
    iteration += 1
    print "result", result
    # Stop iterating after max_iterations
    if iteration >= max_iterations:
        timer.stop()
        print "Output is", result
    else:
        result = get_next(result)
   

# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(13)
timer.start()