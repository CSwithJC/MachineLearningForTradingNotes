""" Accessing array elements """

import numpy as np

def test_run():
    a = np.random.rand(5, 4)
    print "Array:\n", a

    # Accessing element at position (3, 2)
    element = a[3, 2]
    print element

    # Elements in a defined range
    print a[0, 1:3] # this excludes the third column

    # Top-left corner of array
    print a[0:2, 0:2]

    # Slicing
    # Note: Slice n:m:t specifies a range that starts at n, and stops before m, in
    print a[:, 0:3:2] # will select columns 0, 2 for every row
    # so the 2 is the "step" of the loop searching the array



if __name__ == "__main__":
    test_run()