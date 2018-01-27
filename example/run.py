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
		bubble_assign_graph.append([vector_size,np.mean(bubble_assigns)])
		print("Avg bubblesort conditions:" + str(np.mean(bubble_conds)))
		bubble_cond_graph.append([vector_size,np.mean(bubble_conds)])

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
		quick_assign_graph.append([vector_size,np.mean(quick_assigns)])
		print("Avg quicksort conditions:" + str(np.mean(quick_conds)))
		quick_assign_graph.append([vector_size,np.mean(quick_assigns)])

	# plotting number of assignments as function of list size
	t = np.arange(0,1000,10)
	plt.xlabel("List Size")
	plt.ylabel("Assignments")
	plt.plot(bubble_assign_graph, 'rs')
	plt.plot(t,t**2,'r')
	plt.annotate('Bubble Sort', xy=(900, 640000), xytext=(900, 500000),arrowprops=dict(facecolor='black', shrink=0.05))
	plt.plot(quick_assign_graph, 'bo')
	plt.plot(t,t*math.log(t),'b')
	plt.annotate('Quick Sort', xy=(900, 6000), xytext=(900, 5000),arrowprops=dict(facecolor='black', shrink=0.05))
	plt.show()
	
	# plotting number of conditionals as function of list size
	plt.xlabel("List Size")
	plt.ylabel("Assignments")
	plt.plot(bubble_cond_graph, 'rs')
	plt.plot(t,t**2,'r')
	plt.annotate('Bubble Sort', xy=(900, 640000), xytext=(900, 500000),arrowprops=dict(facecolor='black', shrink=0.05))
	plt.plot(quick_cond_graph, 'bo')
	plt.plot(t,t*math.log(t),'b')
	plt.annotate('Quick Sort', xy=(900, 6000), xytext=(900, 5000),arrowprops=dict(facecolor='black', shrink=0.05))
	plt.show()