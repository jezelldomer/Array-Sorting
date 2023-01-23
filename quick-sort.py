# Quick sort 

# function to find the partition position
def partition(array, low, high):

  pivot = array[high]

  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1

      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:

    element = partition(array, low, high)
    quickSort(array, low, element - 1)
    quickSort(array, element + 1, high)

data = [ 2, 27, 40, 7, 13, 66, 1, 31, 41, 24 ]
print("\033[0;33;40m╭─ ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧.˚ₓₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧.˚ₓₓ ─╮\n")
print("             \033[1;37;40m Original Array:")
print("\n    \033[0;34;47m",data)

size = len(data)
print("\033[0;35;40m\n︵‿︵‿୨♡୧‿︵‿︵︵‿︵‿୨♡୧‿︵‿︵︵‿︵‿୨♡୧‿︵‿︵")
quickSort(data, 0, size - 1)

print('\n\033[1;37;40mSorted Array in Ascending Order using Quicksort:\n')
print("    \033[0;34;47m",data)
print("\033[0;33;40m\n╰─ ₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧.˚ₓₓ˚. ୭ ˚○◦˚.˚◦○˚ ୧.˚ₓₓ ─╯\n\033[0;37;40m")