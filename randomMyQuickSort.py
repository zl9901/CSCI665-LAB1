
import numpy as np
import time
import random

"""
InsertionSort function which is used for InsertionSort algorithm
"""
def InsertionSort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key

"""
quickSort algorithm combined with InsertionSort algorithm
"""
def MyQuickSort(arr,low ,high):

    if high-low< 16:
        return

    if low<high:
        x=arr[high-1]
        i=low
        j=high-1
        while i < j:
            while arr[i]<x and i<high-1:
                i+=1
            while arr[j]>=x and j>low:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        q=i
        arr[high-1],arr[q]=arr[q],arr[high-1]

        if low != q : MyQuickSort(arr, low, q)
        if q+1 != high : MyQuickSort(arr, q + 1, high)


"""
This function is being used to generate random real number set
and get the final result
"""
def randomList():
    array = []
    for index in range(1000):
        array.append(random.randint(1, 1001))
    brr = array


    f4 = open("randomList.txt", "a")
    for j in range(len(brr)):
        f4.write(str(brr[j]))
        f4.write("\n")

    low = 0
    high = len(brr)

    print("randomList MyQuickSort time")
    start_time = time.time()
    MyQuickSort(brr, low, high)
    InsertionSort(brr)
    end_time = time.time()
    print("the time is " + str(end_time - start_time))


if __name__ == '__main__':
    randomList()