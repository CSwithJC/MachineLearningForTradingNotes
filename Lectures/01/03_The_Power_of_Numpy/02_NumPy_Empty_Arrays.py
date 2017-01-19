""" Creating NumPy Arrays. """

import numpy as np

def test_run():
    # Empty Array
    print np.empty(5) # 5 rows; this prints very small numbers, not exact 0s.

    print np.empty((5, 4)) # 5 rows, 4 columns

    # print np.empty((5, 4, 3)) # 3 dimensions

    # Array of 1s
    print np.ones((5, 4)) # 5 rows, 4 columns



if __name__ == "__main__":
    test_run()