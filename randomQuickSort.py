
import numpy as np
import matplotlib.pyplot as plt
import time


"""
quickSort algorithm without InsertionSort algorithm
"""
def QuickSort(array,low ,high):

    if low<high :
        x=array[high-1]
        i=low
        j=high-1

        while i < j:
            while array[i]<x and i<high-1:
                i+=1
            while array[j]>=x and j>low:
                j-=1
            if i<j:
                array[i],array[j]=array[j],array[i]
        q=i
        array[high-1],array[q]=array[q],array[high-1]


        if low != q : QuickSort(array, low, q)
        if q+1 != high: QuickSort(array, q + 1, high)

"""
This function is being used to generate random real number set
and get the final result
"""
def randomList():
    array = []
    filename = "randomList.txt"
    with open(filename) as f2:
        num = f2.readline()
        while num != "":
            array.append(int(num))
            num = f2.readline()

    low = 0
    high = len(array)

    print("randomList QuickSort time")
    start_time = time.time()
    QuickSort(array, low, high)
    end_time = time.time()

    print("the time is " + str(end_time - start_time))

if __name__ == '__main__':
    randomList()





