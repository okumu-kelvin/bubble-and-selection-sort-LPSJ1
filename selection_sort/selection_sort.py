import random

def selection_sort(array):
    # TODO: Implement selection sort
    number = len(array)
    for i in range(number):
       min_index = i
       for j in range(i + 1, number):
           if array[j] < array[min_index]:
               min_index = j

       array[i], array[min_index] = array[min_index], array[i]
    
    return array

randie_array = [random.randint(1,15) for _ in range(20)]
print("Unsorted:",randie_array)

sorted_array = selection_sort(randie_array)
print("Sorted:", sorted_array)