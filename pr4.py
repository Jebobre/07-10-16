__author__ = 'student'
import random
import matplotlib.pyplot as plt
import numpy as np

def  get_percentile(values, bucket_number):
    a=[0.0]
    for i in range(1,bucket_number):
        a.append(np.percentile(values,100/bucket_number*i))
    return a

def get_percentile_number(value, percentiles):
    a=0
    for i in range(1,len(percentiles)):
        if percentiles[i]<=value:
            a+=1
    return a


def value_equalization(value,percentiles,add_random=False):
    idx = get_percentile_number(value, percentiles)
    step = 1/len(percentiles)
    if add_random==True:
        random_noise=random.uniform(idx*step,(random.random()+idx)*step)
        new_value=idx*step+random_noise
    else:
        new_value = idx*step
    return new_value



values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
percentiles=get_percentile(values, 5)
print(percentiles)
print(value_equalization(5.5,percentiles,add_random=True),value_equalization(5.5,percentiles,add_random=True))