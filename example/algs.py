import numpy as np

def bubblesort(x):
    """
    Bubble sort: iterate through list n times, swapping adjacent neighbors if they are out of order
    """
	assignments = 0
	conditionals = 0
	length = len(x)
	if length < 2:
		return x
	for iteration in range(length-1):
		for index in range(length-1):
			conditionals += 1
			if x[index] >= x[index+1]:
				assignments += 3
				new_value = x[index+1]
				x[index+1] = x[index]
				x[index] = new_value
	return x, assignments, conditionals
	
def quicksort(x, low, high, cond, assign):
    """
    Quick sort: divide and conquer - partitioning and recursing over pieces
    """
	cond += 1
	if low < high:
		assign += 1
		pivot, cond, assign = partition(x, low, high, cond, assign)
		print("pivot"+str(pivot))
		x, cond, assign = quicksort(x, low, pivot-1, cond, assign)
		x, cond, assign = quicksort(x, pivot+1, high, cond, assign)
	return x, cond, assign

def partition(x, low, high, cond, assign):
	"""
	Partition function for quick sort
	"""
	print(x)
	assign += 3
	pivot_item = x[low]
	print("partition "+str(pivot_item)+' '+str(low)+' '+str(high))
	left = low
	right = high
	while left < right:
		cond += 1
		while x[left] <= pivot_item:
			cond += 1
			assign += 1
			left += 1
		while x[right] > pivot_item:
			cond += 1
			assign += 1			
			right -= 1
		cond += 1
		if left < right:
			assign += 3
			holder = x[left]
			x[left] = x[right]
			x[right] = holder
	assign += 2
	x[low] = x[right]
	x[right] = pivot_item
	return right, cond, assign
