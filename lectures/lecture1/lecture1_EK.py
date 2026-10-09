"""
Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().


3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().
"""



import numpy as np

def argmax(values):
    N = len(values)

    imax = None
    vmax = -np.inf

    for i in range(N):
        value = values[i]
        if value > vmax:      # FIX 1: compare to vmax, not max
            imax = i          # FIX 2: store index i, not 1
            vmax = value

    return imax               # FIX 3: return AFTER loop

values = [2, 3, -1, 7, 4]
imax = argmax(values)
print(f'The maximum is located at {imax}')

j = np.argmax(values)
print(f'The maximum is located at {j}')
