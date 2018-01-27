import numpy as np
from example import algs

def test_bubblesort():
	x = []
	sorted, assign, cond = algs.bubblesort(x)
	assert sorted == []
	x = [1]
	sorted, assign, cond = algs.bubblesort(x)
	assert sorted == [1]
	x = [2,5,1,0,2]
	sorted, assign, cond = algs.bubblesort(x)
	assert sorted == [0,1,2,2,5]



def test_quicksort():
	x = []
	sorted, assign, cond = algs.quicksort(x,0,len(x)-1,0,0)
	assert sorted == []
	x = [1]
	sorted, assign, cond = algs.quicksort(x,0,len(x)-1,0,0)
	assert sorted == [1]
	x = [2,5,1,0,2]
	sorted, assign, cond = algs.quicksort(x,0,len(x)-1,0,0)
	assert sorted == [0,1,2,2,5]