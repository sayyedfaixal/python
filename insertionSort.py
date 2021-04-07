def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while(j>=0 and arr[j]>key):     #while(j>=0 and arr[j]<key)   sorting in descending order
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key


data = [5, 2, 4, 6, 1, 3]
insertionSort(data)
print(data)

