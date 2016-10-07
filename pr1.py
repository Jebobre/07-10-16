__author__ = 'student'
import random
import matplotlib.pyplot as plt
import numpy as np

def  get_percentile(values, bucket_number):
    a=[0.0]
    for i in range(1,bucket_number):
        a.append(np.percentile(values,100/bucket_number*i))
    return a

values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
print(get_percentile(values, 4))