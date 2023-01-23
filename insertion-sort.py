# Insertion sort 

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # using > to sort in ascending order
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key


data = [ 2, 27, 40, 7, 13, 66, 1, 31, 41, 24 ]
insertionSort(data)
print ("\033[0;35;40m-ˋˏ✄┈┈┈┈-ˋˏ✄┈┈┈┈-ˋˏ✄┈┈┈┈-ˋˏ✄┈┈┈┈-ˋˏ✄┈┈┈┈-ˋˏ✄┈┈┈┈-ˋˏ✄┈┈┈┈ˋˏ✄┈┈┈┈\n")
print('    \033[1;37;40mSorted Array in Ascending Order using Insertion Sort:\033[1;37;40m\n')
print("          \033[0;37;42m",data,"\033[0;37;40m\n")