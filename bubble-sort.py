# Bubble sort 

def bubbleSort(array):
    
  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):

    # Using > to sort in ascending order
      if array[j] > array[j + 1]:

        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp