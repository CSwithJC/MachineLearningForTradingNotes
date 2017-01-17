''' Creating NumPy Arrays '''

import numpy as np

def get_max_index(a):
    ''' Return the index of the maximum value in a given 1D array '''
    return a.argmax()

def test_run():

    # List to 1D array
    #print np.array([2, 3, 4])
    # List to 2D array
    #print np.array([(2, 3, 4), (5, 6, 7)])

    # Empty array
    #print np.empty(5)
    #print np.empty((5, 4)) #has lots of random values that were in memory

    # Array of 1s
    #print np.ones((5, 4))

    # Specifying the datatype
    #print np.ones((5, 4), dtype=np.int_)

    # Generate array full of random numbers, uniformly sampled from [0.0, 1.0]
    #print np.random.random((5, 4)) # pass in a size sample

    # Sample numbers from a Gaussian (normal) distribution
    #print np.random.normal(size=(2, 3)) # "standard normal" (mean = 0, s.d. = 1)
    #print np.random.normal(50, 10, size=(2, 3)) # (mean = 50, s.d. = 10)

    # Random Integers
    #print np.random.randint(10) # a single integer in [0, 10)
    #print np.random.randint(0, 10) # same as above, specifying [low, high] explicit
    #print np.random.randint(0, 10, size=5) # 5 random integers as a 1D array
    #print np.random.randint(0, 10, size=(2, 3)) # 2x3 array of random integers

    #a = np.random.random((5, 4)) # 5x4 array of random numbers
    #print a
    #print a.shape
    #print a.shape[0] # number of rows
    #print a.shape[1] # number of columns
    #print a.size
    #print a.type

    np.random.seed(693) #seed the random number generator
    a = np.random.randint(0, 10, size=(5, 4)) # 5x4 random integers in [0,10)
    print "Array:\n", a

    # Sum of all elements
    print "Sum of all elements:", a.sum()

    # Iterate over rows, to compute sum of each column
    print "Sum of each column:\n", a.sum(axis=0)

    # Iterate over columns to compute sum of each row
    print "Sum of each row:\n", a.sum(axis=1)

    # Statistics: min, max, mean (across rows, cols, and overall)
    print "Minimum of each column:\n", a.min(axis=0)
    print "Maximum of each row:\n", a.max(axis=1)
    print "Mean of all elemens:", a.mean() # leave out axis

    a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0), (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    print a

    # calculate mean
    mean = a.mean()
    print mean

    #masking
    print a[a<mean]

    a[a < mean] = mean
    print a

if __name__ == "__main__":
    test_run()