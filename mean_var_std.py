import numpy as np

def calculate(list):

    ls= np.array(list)

    mean1 = [ls[[0, 1, 2]].mean(), ls[[3, 4, 5]].mean(), ls[[6, 7, 8]].mean()]
    mean2 = []

    return {

        'mean': [axis1, axis2, flattened],
        'variance': [axis1, axis2, flattened],
        'standard deviation': [axis1, axis2, flattened],
        'max': [axis1, axis2, flattened],
        'min': [axis1, axis2, flattened],
        'sum': [axis1, axis2, flattened]

    }
