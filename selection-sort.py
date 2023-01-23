# Selection sort 

def selectionSort(array, size):
   
    for step in range(size):
        minpos = step

        for i in range(step + 1, size):
         
            # using < to sort in ascending order
            if array[i] < array[minpos]:
                minpos = i
                         
        (array[step], array[minpos]) = (array[minpos], array[step])

# arrays in the spreadsheet 
data = [ 2, 27, 40, 7, 13, 66, 1, 31, 41, 24 ]
size = len(data)
selectionSort(data, size)
print ("\033[1;33;40m╭── ⋅ ⋅ ── ✩ ── ⋅ ⋅─── ⋅ ⋅ ── ✩ ── ⋅ ⋅─── ⋅ ⋅ ── ✩ ── ⋅ ⋅──╮\033[1;33;40m\n")
print('   \033[1;37;40mSorted Array in Ascending Order using Selection Sort:\033[1;37;40m\n')
print("         \033[0;37;44m",data,"\033[0;37;40m\n")
