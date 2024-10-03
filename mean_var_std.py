import numpy as np

def calculate(list):

#Create list
    ls= np.array(list)
#Only allow input of 9 elements
    if len(list) != 9: 
        raise ValueError("List must contain nine numbers.")   

#Convert list to 3x3 np array
    np_arr = ls.reshape(3,3): 
      
#Calculate mean
    mean1 = [np_arr[[0, 1, 2]].mean(), np_arr[[3, 4, 5]].mean(), np_arr[[6, 7, 8]].mean()]
    mean2 = [np_arr[[0, 3, 6]].mean(), np_arr[[1, 4, 7]].mean(), np_arr[[2, 5, 8]].mean()] 

#Calculate variance
    var1 = [np_arr[[0, 1, 2]].var(), np_arr[[3, 4, 5]].var(), np_arr[[6, 7, 8]].var()]
    var2 = [np_arr[[0, 3, 6]].var(), np_arr[[1, 4, 7]].var(), np_arr[[2, 5, 8]].var()]

#Calculate standard-deviation
    stand_dev1 = [np_arr[[0, 1, 2]].std(), np_arr[[3, 4, 5]].std(), np_arr[[6, 7, 8]].std()]
    stand_dev2 = [np_arr[[0, 3, 6]].std(), np_arr[[1, 4, 7]].std(), np_arr[[2, 5, 8]].std()]

#Calculate maximum
    max1 = [np_arr[[0, 1, 2]].max(), np_arr[[3, 4, 5]].max(), np_arr[[6, 7, 8]].max()]
    max2 = [np_arr[[0, 3, 6]].max(), np_arr[[1, 4, 7]].max(), np_arr[[2, 5, 8]].max()]

#Calculate minimum
    min1 = [np_arr[[0, 1, 2]].min(), np_arr[[3, 4, 5]].min(), np_arr[[6, 7, 8]].min()]
    min2 = [np_arr[[0, 3, 6]].min(), np_arr[[1, 4, 7]].min(), np_arr[[2, 5, 8]].min()]

#Calcualte total
    sum1 = [np_arr[[0, 1, 2]].sum(), np_arr[[3, 4, 5]].sum(), np_arr[[6, 7, 8]].sum()]
    sum2 = [np_arr[[0, 3, 6]].sum(), np_arr[[1, 4, 7]].sum(), np_arr[[2, 5, 8]].sum()]


    calculations = {'mean': [mean1.tolist(), mean2.tolist(), (np_arr.mean()).tolist()],
                    'variance': [var1.tolist(), var2.tolist(), (np_arr.var()).tolist()],
                    'standard deviation': [stand_dev1.tolist(), stand_dev2.tolist(), (np_arr.std()).tolist()],
                    'max': [max1.tolist(), max2.tolist(), (np_arr.max()).tolist()],
                    'min': [min1.tolist(), min2.tolist(), (np_arr.min()).tolist()],
                    'sum': [sum1.tolist(), sum2.tolist(), (np_arr.sum()).tolist()]
                   }

    return calculations

print (calculate([0,1,2,3,4,5,6,7,8]))
