__author__ = 'student'
import random
import matplotlib.pyplot as plt
import numpy as np

def  get_percentile(values, bucket_number):
    a=[0.0]
    for i in range(1,bucket_number):
        a.append(np.percentile(values,100/bucket_number*i))
    return a
get_percentile_number(value, percentiles)

percentiles=get_percentile(values, 4)
print(percentiles)
print(get_percentile_number(2.5,percentiles))
print(get_percentile_number(5.5,percentiles))
print(get_percentile_number(100,percentiles))