
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

    if high-low< 100:
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
PoissonDistribution function
which is being used to generate Poisson distribution data
and get the result
"""
def PoissonDistribution():

    lamda = 500
    poisson = np.random.poisson(lamda, 1000)

    array = []
    for i in range(0, len(poisson)):
        array.append(poisson[i])
    arr=array

    f3 = open("poissonOutput.txt", "a")
    for j in range(len(arr)):
        f3.write(str(arr[j]))
        f3.write("\n")

    low = 0
    high = len(arr)

    print("Poisson MyQuickSort time")
    start_time = time.time()
    MyQuickSort(arr, low, high)
    InsertionSort(arr)
    end_time = time.time()
    print("the time is " + str(end_time - start_time))


if __name__ == '__main__':
    PoissonDistribution()
