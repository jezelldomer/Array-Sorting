# Merge Sort 

def mergeSort(array):
    if len(array) > 1:

        d = len(array)//2
        L = array[:d]
        M = array[d:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            
            
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
    
if __name__ == '__main__':
    array = [ 2, 27, 40, 7, 13, 66, 1, 31, 41, 24 ]

    mergeSort(array)

    print ("\033[0;35;40m✼ ҉ ✼-- ҉ ✼✼-- ҉ ✼-- ҉ ✼✼-- ҉ ✼-- ҉ ✼✼-- ҉ ✼-- ҉ ✼✼-- ҉ ✼-- ҉ \n")    
    print('\033[1;37;40mSorted Array in Ascending Order using Merge Sort:\033[1;33;40m\n')
    printList(array)
    print('\n')