import functions as func
     
if __name__ == '__main__':
    len_data = 200
    scale = 2
    in_data = func.generate_data(len_data = len_data, scale = scale)
    shuffled_data = func.shuffle_data(in_data)
    sorted_data = func.bubble_sort(shuffled_data)