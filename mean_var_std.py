import numpy as np

def calculate(list):

    ls= np.array(list)
    

#Calculate mean
    mean1 = [ls[[0, 1, 2]].mean(), ls[[3, 4, 5]].mean(), ls[[6, 7, 8]].mean()]
    mean2 = [ls[[0, 3, 6]].mean(), ls[[1, 4, 7]].mean(), ls[[2, 5, 8]].mean()] 

#Calculate variance
    var1 = [ls[[0, 1, 2]].var(), ls[[3, 4, 5]].var(), ls[[6, 7, 8]].var()]
    var2 = [ls[[0, 3, 6]].var(), ls[[1, 4, 7]].var(), ls[[2, 5, 8]].var()]

#Calculate standard-deviation
    stand_dev1 = [ls[[0, 1, 2]].std(), ls[[3, 4, 5]].std(), ls[[6, 7, 8]].std()]
    stand_dev2 = [ls[[0, 3, 6]].std(), ls[[1, 4, 7]].std(), ls[[2, 5, 8]].std()]

#Calculate maximum
    max1 = [ls[[0, 1, 2]].max(), ls[[3, 4, 5]].max(), ls[[6, 7, 8]].max()]
    max2 = [ls[[0, 3, 6]].max(), ls[[1, 4, 7]].max(), ls[[2, 5, 8]].max()]

#Calculate minimum
    min1 = [ls[[0, 1, 2]].min(), ls[[3, 4, 5]].min(), ls[[6, 7, 8]].min()]
    min2 = [ls[[0, 3, 6]].min(), ls[[1, 4, 7]].min(), ls[[2, 5, 8]].min()]

#Calcualte total
    sum1 = [ls[[0, 1, 2]].sum(), ls[[3, 4, 5]].sum(), ls[[6, 7, 8]].sum()]
    sum2 = [ls[[0, 3, 6]].sum(), ls[[1, 4, 7]].sum(), ls[[2, 5, 8]].sum()]



    return {

        'mean': [mean1, mean2, ls.mean()],
        'variance': [var1, var2, ls.var()],
        'standard deviation': [stand_dev1, stand_dev2, ls.std()],
        'max': [max1, max2, ls.max()],
        'min': [min1, min2, ls.min()],
        'sum': [sum1, sum2, ls.sum()]

    }
