import matplotlib.pyplot as plt
import numpy as np

def generate_data(len_data=100,scale=1.0):
    '''
    Generating of linear data.

    Parameters
    ----------
    len_data : int, optional
        Lenght of x-axis. The default is 100.
    scale : float, optional
        Change y-axis range form 0 to len_data*scale. The default is 1.

    Returns
    -------
    array
        returns linear data.

    '''
    return np.arange(len_data)*scale

def shuffle_data(data):
    '''
    Random data shuffling.

    Parameters
    ----------
    data : array
        Data to shuffle.

    Returns
    -------
    data : array
        Shuffled array.

    '''
    ### Get data lenght
    n = len(data)
    ### Parameter to get more shuffled data
    shuffle_loop = 5
    for _ in range(shuffle_loop):
        for _ in range(n):
            ### Get random indexes of first and second element from array
            first = np.random.randint(0,n,1)[0]
            sec = np.random.randint(0,n,1)[0]
            ### Prevent of get the same elements
            if first != sec:
                ### Data shuffle
                data[sec],data[first]= data[first], data[sec]
    return data

def bubble_sort(data):
    ### Init plot
    plt.figure()
    ### Start sorting loop
    while True:
        ### Create state list
        state = []
        ### Get data lenght
        n = len(data)
        for i in range(n-1):
            ### Check two elements  in array
            if data[i]>data[i+1]:
                ### Swap elements in array
                data[i+1],data[i]= data[i], data[i+1]
                ### Get data to state list
                state.append(1)
            else:
                ### Get data to state list
                state.append(0)
        ### Clean plot
        plt.clf()
        ### Display data
        plt.title('Bubble sort',fontsize = 16)
        plt.scatter(np.arange(n),data,s = 8)
        plt.xlabel('# of index',fontsize = 12)
        plt.ylabel('Amplitude',fontsize = 12)
        plt.pause(0.06)
        ### If state sum is equal to 0 it means that all data is sorted 
        if sum(state) == 0:
            return data
            break
    plt.show()