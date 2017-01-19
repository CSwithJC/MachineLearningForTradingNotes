""" Array Attributes """

import numpy as np

def test_run():

    a = np.random.random((5, 4)) # 5x4 array of random numbers
    print a
    print a.shape # prints the shape of the array (here, prints (5,4))
    print a.shape[0] # number of rows
    print a.shape[1] # number of columns

    print len(a.shape) # prints 2, since that is the dimention of (5,4)

    print a.size # prints the number of elements in the array(here, prints 20, or 5*4)

    print a.dtype # prints the type of the elements in the array

if __name__ == "__main__":
    test_run()