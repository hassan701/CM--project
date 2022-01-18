import time 
import random

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
           
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
def create_array(size):
    array = [0]

    for i in range(1, size):
        num = array[i-1] + random.randint(1, 10)
        array.append(num)

    return array

size = [32, 128]
durations = []

for i in range(len(size)):
    times = 0
    for f in range(5):
        array = create_array(size[i])
        tg = time.time_ns()
        result = selectionSort(array)
        times += time.time_ns() - tg  

    durations.append(times/5)


print(durations)
print("Ratio for 32 and 128 is",durations[0]/durations[1])