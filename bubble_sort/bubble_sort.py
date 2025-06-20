import random

def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort

    number = len(unsorted_list)
    for i in range(number):
        for j in range(0, number - i - 1):
            if unsorted_list[j] > unsorted_list[j +1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list  
    
ran_array= [random.randint(1,1000) for _ in range(20)]
print("Unsorted array:", ran_array)

sorted_array=bubble_sort(ran_array)
print("Sorted array:", sorted_array)
    

