import numpy as np
from example import algs

def test_bubblesort():
    x = np.array([1,2,4,0,1])
    sorted, assign, cond = algs.bubblesort(x)
    assert sorted = x.sort()

def test_quicksort():
    x = np.array([1,2,4,0,1])
    sorted, assign, cond = algs.bubblesort(x,0,len(x)-1,0,0))
    assert sorted = x.sort()