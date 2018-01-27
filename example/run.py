"""
Andrew Kung
BMI203 HW #1
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from .algs import quicksort, bubblesort, partition

def run_stuff():
	"""
	This function is called in `__main__.py`
	"""
	
	vector_sizes = [100,200,300,400,500,600,700,800,900,1000]
	number_tests = 100

	bubble_assign_graph = []
	bubble_cond_graph = []

	for vector_size in vector_sizes:
		bubble_assigns = []
		bubble_conds = []
		for iteration in range(number_tests):
			sort_list = np.random.rand(vector_size)
			bubble_sorted, bubble_assign, bubble_cond = bubblesort(sort_list)
			bubble_assigns.append(bubble_assign)
			bubble_conds.append(bubble_cond)
		print("List size:" + str(vector_size))
		print("Avg bubblesort assignments:" + str(np.mean(bubble_assigns)))
		bubble_assign_graph.append(np.mean(bubble_assigns))
		print("Avg bubblesort conditions:" + str(np.mean(bubble_conds)))
		bubble_cond_graph.append(np.mean(bubble_conds))

	quick_assign_graph = []
	quick_cond_graph = []

	for vector_size in vector_sizes:
		quick_assigns = []
		quick_conds = []
		for iteration in range(number_tests):
			sort_list = np.random.rand(vector_size)
			quick_sorted, quick_assign, quick_cond = quicksort(sort_list)
			quick_assigns.append(quick_assign)
			quick_conds.append(quick_cond)
		print("List size:" + str(vector_size))
		print("Avg quicksort assignments:" + str(np.mean(quick_assigns)))
		quick_assign_graph.append(np.mean(quick_assigns))
		print("Avg quicksort conditions:" + str(np.mean(quick_conds)))
		quick_assign_graph.append(np.mean(quick_assigns))
		
	# plotting number of assignments as function of list size
	t = np.arange(0,1000,10)

	plt.xlabel("List Size")
	plt.title("Assignments")
	plt.plot(lengths, bubble_assign_graph, 'rs')
	plt.plot(t,0.5*t**2,'r')
	plt.annotate('Bubble Sort: O(n^2)', xy=(700, 250000), xytext=(550, 400000),arrowprops=dict(facecolor='black', shrink=0.05))
	plt.plot(lengths, quick_assign_graph, 'bo')
	plt.plot(t,2.5*t*np.log(t),'b')
	plt.annotate('Quick Sort: O(n log n)', xy=(800, 20000), xytext=(700, 100000),arrowprops=dict(facecolor='black', shrink=0.05))
	plt.show()

	# plotting number of conditionals as function of list size
	plt.xlabel("List Size")
	plt.title("Conditionals")
	plt.plot(lengths, bubble_cond_graph, 'rs')
	plt.plot(t,t**2,'r')
	plt.annotate('Bubble Sort: O(n^2)', xy=(700, 500000), xytext=(550, 800000),arrowprops=dict(facecolor='black', shrink=0.05))
	plt.plot(lengths, quick_cond_graph, 'bo')
	plt.plot(t,3*t*np.log(t),'b')
	plt.annotate('Quick Sort: O(n log n)', xy=(800, 20000), xytext=(700, 150000),arrowprops=dict(facecolor='black', shrink=0.05))
	plt.show()