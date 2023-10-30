import random
import time 
import sys
import matplotlib.pyplot as plt
# overiding the default recursion limit of ubuntu
sys.setrecursionlimit(10000)
# insertion sort
def insertion_sort(unsorted_list):
    size_of_list = len(unsorted_list)
    start_time=time.process_time()
    for i in range(size_of_list):
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp
    end_time=time.process_time()
    return end_time-start_time
# quick sort
def swap( A, x, y ):
    temp= A[x]
    A[x] = A[y]
    A[y] = temp
def Partition( A, low, high ) :
    pivot= low
    swap( A, pivot, high)
    for i in range(low, high ):
        if A[i]<=A[high]:
            swap( A, i, low)
            low+=1
    swap( A, low, high)
    return low
def quick_sort(unsorted_list,low,high):
    start_time=time.process_time()
    if low < high:
        pivot = Partition( unsorted_list, low, high)
        quick_sort( unsorted_list, low, pivot - 1 )
        quick_sort( unsorted_list, pivot + 1, high)
    end_time=time.process_time()
    return end_time-start_time
# merge sort
def merge_sort(unsorted_list):
    start_time=time.process_time()
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
        while i<len(left):
             unsorted_list[k]=left[i]
             i=i+1
             k=k+1
        while j<len(right):
             unsorted_list[k]=right[j]
             j=j+1
             k=k+1
    end_time=time.process_time()
    return end_time-start_time

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
    size_elapsed_time={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"asc")
             elapsed_time=quick_sort(numbers,0,size-1)
             size_elapsed_time[size]=elapsed_time      
    return size_elapsed_time 
def analyse_quick_sort_des(size_num_inputs):
    size_elapsed_time={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"des")
             elapsed_time=quick_sort(numbers,0,size-1)
             size_elapsed_time[size]=elapsed_time      
    return size_elapsed_time 
def analyse_quick_sort_rand(size_num_inputs):
    size_elapsed_time={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"rand")
             elapsed_time=quick_sort(numbers,0,size-1)
             size_elapsed_time[size]=elapsed_time      
    return size_elapsed_time 
# insertion sort
def analyse_insertion_sort_asc(size_num_inputs):
    size_elapsed_time={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"asc")
             elapsed_time=insertion_sort(numbers)
             size_elapsed_time[size]=elapsed_time      
    return size_elapsed_time 
def analyse_insertion_sort_des(size_num_inputs):
    size_elapsed_time={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"des")
             elapsed_time=insertion_sort(numbers)
             size_elapsed_time[size]=elapsed_time      
    return size_elapsed_time 
def analyse_insertion_sort_rand(size_num_inputs):
    size_elapsed_time={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"rand")
             elapsed_time=insertion_sort(numbers)
             size_elapsed_time[size]=elapsed_time      
    return size_elapsed_time 

# merge sort 
 
def analyse_merge_sort_asc(size_num_inputs):
    size_elapsed_time={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"asc")
             elapsed_time=merge_sort(numbers)
             size_elapsed_time[size]=elapsed_time      
    return size_elapsed_time 
def analyse_merge_sort_des(size_num_inputs):
    size_elapsed_time={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"des")
             elapsed_time=merge_sort(numbers)
             size_elapsed_time[size]=elapsed_time      
    return size_elapsed_time 
def analyse_merge_sort_rand(size_num_inputs):
    size_elapsed_time={}
    for size in size_num_inputs:
             numbers=generate_data_by_order(size,"rand")
             elapsed_time=merge_sort(numbers)
             size_elapsed_time[size]=elapsed_time      
    return size_elapsed_time 



def plot(title,asc,des,rand):
    plt.title(title)
    plt.xlabel("Number of inputs")
    plt.ylabel("Time in millis")
    plt.plot(asc.keys(),asc.values())
    plt.plot(des.keys(),des.values())
    plt.plot(rand.keys(),rand.values())
    plt.grid(True)
    plt.legend(["Assending","Desending","Random"],loc=2)
    plt.savefig("images/time/"+title+".png")
    plt.show()
def plot_all(title,ins_rand,qui_rand,mer_rand):
    plt.title(title)
    plt.xlabel("Number of inputs")
    plt.ylabel("Time in millis")
    plt.plot(ins_rand.keys(),ins_rand.values())
    plt.plot(qui_rand.keys(),qui_rand.values())
    plt.plot(mer_rand.keys(),mer_rand.values())
    plt.grid(True)
    plt.legend(["Insertion sort","Quick Sort","Merege Sort"],loc=2)
    plt.savefig("images/time/"+title+".png")
    plt.show()
def main():
    num_inputs=[i for i in range(100,10000,1000)]
    # quick sort analysis
    quick_asc_time=analyse_quick_sort_asc(num_inputs)
    quick_des_time=analyse_quick_sort_des(num_inputs)
    quick_rand_time=analyse_quick_sort_rand(num_inputs)
    plot("Quick Sort",quick_asc_time,quick_des_time,quick_rand_time)
    # insertion sort analysis
    insertion_asc_time=analyse_insertion_sort_asc(num_inputs)
    insertion_des_time=analyse_insertion_sort_des(num_inputs)
    insertion_rand_time=analyse_insertion_sort_rand(num_inputs)
    plot("Insertion Sort",insertion_asc_time,insertion_des_time,insertion_rand_time)
    # merge sort analysis
    merge_asc_time=analyse_merge_sort_asc(num_inputs)
    merge_des_time=analyse_merge_sort_des(num_inputs)
    merge_rand_time=analyse_merge_sort_rand(num_inputs)
    plot("Merge Sort",merge_asc_time,merge_des_time,merge_rand_time)
    plot_all("All in one",
       insertion_rand_time
         ,quick_rand_time
        ,merge_rand_time,)
   
main()
      
        


