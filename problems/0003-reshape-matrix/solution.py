import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    if ((len(a) * len(a[0])) != (new_shape[0] * new_shape[1])):
        return []
    
    a = np.array(a)
    a = np.ravel(a)
    reshaped_matrix = np.zeros((new_shape[0], new_shape[1]))

    counter = 0

    for i in range (new_shape[0]):
        for j in range (new_shape[1]):
            reshaped_matrix[i][j] = a[counter]
            counter += 1

    return reshaped_matrix