# Bubble sort 

def bubbleSort(array):
    
  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):

    # Using < to sort in descending order
    # commited error, now sorting in descending order instead of ascending order
      if array[j] < array[j + 1]:

        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


print ("\033[1;33;40m.. • ☆ . ° .• °:. *₊° .☆. . • ☆ . ° .• °:. *₊° .☆.. • ☆ .\033[1;33;40m\n")       
data = [ 2, 27, 40, 7, 13, 66, 1, 31, 41, 24 ]     
bubbleSort(data)
print('   \033[1;37;40mSorted Array in Descending Order using Bubble Sort:\033[1;37;40m\n')
print("       \033[0;37;41m",data,"\033[0;37;40m\n")
