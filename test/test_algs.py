import numpy as np
from example import algs

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = np.array([1,2,4,0,1])
    
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    sorted, assign, cond = algs.bubblesort(x))
    assert sorted = x.sort()

def test_quicksort():

    x = np.array([1,2,4,0,1])
    # for now, just attempt to call the quicksort function, should
    # actually check output
    sorted, assign, cond = algs.bubblesort(x,0,len(x)-1,0,0))
    assert sorted = x.sort()