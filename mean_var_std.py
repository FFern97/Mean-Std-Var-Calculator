import numpy as np

def calculate(list):

#Create list
    ls= np.array(list)
#Only allow input of 9 elements
    if len(list) != 9: 
        raise ValueError("List must contain nine numbers.")   

#Convert list to 3x3 np array
    np_arr = ls.reshape(3,3)
      
#Calculate mean
    mean1 = np_arr.mean(axis=0).tolist()
    mean2 = np_arr.mean(axis=1).tolist() 
    flat_mean = np_arr.mean()
    
#Calculate variance
    var1 = np_arr.var(axis=0).tolist()
    var2 = np_arr.var(axis=1).tolist() 
    flat_var = np_arr.var()
    
#Calculate standard-deviation
    stand_dev1 = np_arr.std(axis=0).tolist()
    stand_dev2 = np_arr.std(axis=1).tolist() 
    flat_stand_dev = np_arr.std()
    
#Calculate maximum
    max1 = np_arr.max(axis=0).tolist()
    max2 = np_arr.max(axis=1).tolist() 
    flat_max = np_arr.max()
    
#Calculate minimum
    min1 = np_arr.min(axis=0).tolist()
    min2 = np_arr.min(axis=1).tolist() 
    flat_min = np_arr.min()

#Calcualte total
    sum1 = np_arr.sum(axis=0).tolist()
    sum2 = np_arr.sum(axis=1).tolist() 
    flat_sum = np_arr.sum()


    calculations = {'mean': [mean1, mean2, flat_mean],
                    'variance': [var1, var2, flat_var],
                    'standard deviation': [stand_dev1, stand_dev2, flat_stand_dev],
                    'max': [max1, max2, flat_max],
                    'min': [min1, min2, flat_min],
                    'sum': [sum1, sum2, flat_sum]
                   }

    return calculations
