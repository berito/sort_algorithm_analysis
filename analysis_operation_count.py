import random
import time 
import sys
import matplotlib.pyplot as plt
# overiding the default recursion limit of ubuntu

sys.setrecursionlimit(10000)
QUICK_SORT_OPERATIONS=0
MEREGE_SORT_COUNT_OPERATIONS=0
# insertion sort
def insertion_sort(unsorted_list):
    size_of_list = len(unsorted_list)
    count_operations=0
    for i in range(size_of_list):
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp
                count_operations+=1
              
    return count_operations
# quick sort
def swap( A, x, y ):
    temp= A[x]
    A[x] = A[y]
    A[y] = temp
def Partition( A, low, high ) :
    count_operations=0
    pivot= low
    swap( A, pivot, high)
    for i in range(low, high ):
        if A[i]<=A[high]:
            swap( A, i, low)
            low+=1
            count_operations+=1
    swap( A, low, high)
    return low,count_operations
def quick_sort(unsorted_list,low,high):
    global QUICK_SORT_OPERATIONS
    if low < high:
        # return count_operations at each recursive call
        pivot,count_operations = Partition( unsorted_list, low, high)
        QUICK_SORT_OPERATIONS+=count_operations
        quick_sort( unsorted_list, low, pivot - 1 )
        quick_sort( unsorted_list, pivot + 1, high)
    return QUICK_SORT_OPERATIONS
# merge sort
def merge_sort(unsorted_list):
    global MEREGE_SORT_COUNT_OPERATIONS
    if len(unsorted_list) > 1:
        mid = len(unsorted_list)//2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i <len(left) and j<len(right):
            if left[i] < right[j]:
                unsorted_list[k]=left[i]
                i=i+1
            else:
                unsorted_list[k]= right[j]
                j=j+1
            k=k+1
            MEREGE_SORT_COUNT_OPERATIONS+=1
        while i<len(left):
             unsorted_list[k]=left[i]
             i=i+1
             k=k+1
             MEREGE_SORT_COUNT_OPERATIONS+=1
        while j<len(right):
             unsorted_list[k]=right[j]
             j=j+1
             k=k+1
             MEREGE_SORT_COUNT_OPERATIONS+=1
    return MEREGE_SORT_COUNT_OPERATIONS

# data generator 
def generate_data_by_order(size_num_inputs,sort_type="rand"):
    numbers=[random.randint(1,100) for i in range(size_num_inputs)]
    if sort_type=="asc":
        numbers.sort()
    elif sort_type=="des":
        numbers.sort(reverse=True)
    return numbers
# quick sort analysis
def analyse_quick_sort_asc(size_num_inputs):
    size_operation_count={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"asc")
             operation_count=quick_sort(numbers,0,size-1)
             QUICK_SORT_COUNT_OPERATIONS=0
             size_operation_count[size]=operation_count     
    return size_operation_count 
def analyse_quick_sort_des(size_num_inputs):
    size_operation_count={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"des")
             operation_count=quick_sort(numbers,0,size-1)
             QUICK_SORT_COUNT_OPERATIONS=0
             size_operation_count[size]=operation_count      
    return size_operation_count 
def analyse_quick_sort_rand(size_num_inputs):
    size_operation_count={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"rand")
             operation_count=quick_sort(numbers,0,size-1)
             QUICK_SORT_COUNT_OPERATIONS=0
             size_operation_count[size]=operation_count      
    return size_operation_count 
# insertion sort
def analyse_insertion_sort_asc(size_num_inputs):
    size_operation_count={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"asc")
             operation_count=insertion_sort(numbers)
             size_operation_count[size]=operation_count      
    return size_operation_count 
def analyse_insertion_sort_des(size_num_inputs):
    size_operation_count={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"des")
             operation_count=insertion_sort(numbers)
             size_operation_count[size]=operation_count      
    return size_operation_count 
def analyse_insertion_sort_rand(size_num_inputs):
    size_operation_count={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"rand")
             operation_count=insertion_sort(numbers)
             size_operation_count[size]=operation_count      
    return size_operation_count 

# merge sort 
 
def analyse_merge_sort_asc(size_num_inputs):
    size_operation_count={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"asc")
             operation_count=merge_sort(numbers)
             MEREGE_SORT_COUNT_OPERATIONS=0
             size_operation_count[size]=operation_count      
    return size_operation_count 
def analyse_merge_sort_des(size_num_inputs):
    size_operation_count={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"des")
             operation_count=merge_sort(numbers)
             MEREGE_SORT_COUNT_OPERATIONS=0
             size_operation_count[size]=operation_count      
    return size_operation_count 
def analyse_merge_sort_rand(size_num_inputs):
    size_operation_count={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"rand")
             operation_count=merge_sort(numbers)
             MEREGE_SORT_COUNT_OPERATIONS=0
             size_operation_count[size]=operation_count      
    return size_operation_count 



def plot(title,asc,des,rand):
    plt.title(title)
    plt.xlabel("Number of inputs")
    plt.ylabel("Count Operations")
    plt.plot(asc.keys(),asc.values())
    plt.plot(des.keys(),des.values())
    plt.plot(rand.keys(),rand.values())
    plt.grid(True)
    plt.legend(["Assending","Desending","Random"],loc=2)
    plt.savefig("images/count_operation/"+title+".png")
    plt.show()
def plot_all(title,ins_rand,qui_rand,mer_rand):
    plt.title(title)
    plt.xlabel("Number of inputs")
    plt.ylabel("Count Operations")
    plt.plot(ins_rand.keys(),ins_rand.values())
    plt.plot(qui_rand.keys(),qui_rand.values())
    plt.plot(mer_rand.keys(),mer_rand.values())
    plt.grid(True)
    plt.legend(["Insertion sort","Quick Sort","Merege Sort"],loc=2)
    plt.savefig("/images/count_operation"+title+".png")
    plt.show()
def main():
    num_inputs=[i for i in range(100,10000,1000)]
    # quick sort analysis
    quick_asc_count=analyse_quick_sort_asc(num_inputs)
    quick_des_count=analyse_quick_sort_des(num_inputs)
    quick_rand_count=analyse_quick_sort_rand(num_inputs)
    plot("Quick_Sort",quick_asc_count,quick_des_count,quick_rand_count)
    # insertion sort analysis
    insertion_asc_count=analyse_insertion_sort_asc(num_inputs)
    insertion_des_count=analyse_insertion_sort_des(num_inputs)
    insertion_rand_count=analyse_insertion_sort_rand(num_inputs)
    plot("Insertion_Sort",insertion_asc_count,insertion_des_count,insertion_rand_count)
    # merge sort analysis
    merge_asc_count=analyse_merge_sort_asc(num_inputs)
    merge_des_count=analyse_merge_sort_des(num_inputs)
    merge_rand_count=analyse_merge_sort_rand(num_inputs)
    plot("Merge_Sort_Count",merge_asc_count,merge_des_count,merge_rand_count)
    plot_all("All in one by Operation Count",
       insertion_rand_count
         ,quick_rand_count
        ,merge_rand_count)
   
main()
      
        


