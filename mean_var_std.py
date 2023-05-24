import numpy as np

def calculate(numbers_list: list):
    if len(numbers_list) != 9:
        raise ValueError("List must contain nine numbers.")

    numpy_array = np.array([numbers_list[0:3], numbers_list[3:6], numbers_list[6:9]])
    mean_1 = numpy_array.mean(axis=0).tolist()
    mean_2 = numpy_array.mean(axis=1).tolist()
    mean_f = numpy_array.mean()

    var_1 = numpy_array.var(axis=0).tolist()
    var_2 = numpy_array.var(axis=1).tolist()
    var_f = numpy_array.var()

    std_1 = numpy_array.std(axis=0).tolist()
    std_2 = numpy_array.std(axis=1).tolist()
    std_f = numpy_array.std()

    max_1 = numpy_array.max(axis=0).tolist()
    max_2 = numpy_array.max(axis=1).tolist()
    max_f = numpy_array.max()

    min_1 = numpy_array.min(axis=0).tolist()
    min_2 = numpy_array.min(axis=1).tolist()
    min_f = numpy_array.min()

    sum_1 = numpy_array.sum(axis=0).tolist()
    sum_2 = numpy_array.sum(axis=1).tolist()
    sum_f = numpy_array.sum()

    calculations = {
        "mean": [mean_1, mean_2, mean_f],
        "variance": [var_1, var_2, var_f],
        "standard deviation": [std_1, std_2, std_f],
        "max": [max_1, max_2, max_f],
        "min": [min_1, min_2, min_f],
        "sum": [sum_1, sum_2, sum_f]
    }
    
    return calculations