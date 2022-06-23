import functions as func
     
if __name__ == '__main__':
    ### Set lenght data
    len_data = 200
    ### Set scale
    scale = 5
    ### Get linear data to shuffle and sort
    in_data = func.generate_data(len_data = len_data, scale = scale)
    ### Get and plot sorted data
    sorted_data = func.bubble_sort(func.shuffle_data(in_data))