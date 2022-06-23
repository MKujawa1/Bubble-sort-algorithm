import matplotlib.pyplot as plt
import numpy as np

def generate_data(len_data=100,scale=1):
    return np.arange(len_data)*scale

def shuffle_data(data):
    n = len(data)
    shuffle_loop = 2
    for _ in range(shuffle_loop):
        for _ in range(n):
            first = np.random.randint(0,n,1)[0]
            sec = np.random.randint(0,n,1)[0]
            if first != sec:
                data[sec],data[first]= data[first], data[sec]
    return data

def bubble_sort(data):
    plt.figure()
    while True:
        state = []
        n = len(data)
        for i in range(n-1):
            if data[i]>data[i+1]:
                data[i+1],data[i]= data[i], data[i+1]
                state.append(1)
            else:
                state.append(0)
        plt.clf()
        plt.scatter(np.arange(n),data,s = 8)
        plt.pause(0.05)
        if sum(state) == 0:
            return data
            break