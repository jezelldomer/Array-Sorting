# Selection sort 

def selectionSort(array, size):
   
    for step in range(size):
        minpos = step

        for i in range(step + 1, size):
         
            # using < to sort in ascending order
            if array[i] < array[minpos]:
                minpos = i
                         
        (array[step], array[minpos]) = (array[minpos], array[step])


