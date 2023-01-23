# Insertion sort 

def insertionSort(array):

    for step in range(1, len(array)):
        sort = array[step]
        j = sort - 1
        
        # using > to sort in ascending order
        while j >= 0 and sort < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = sort