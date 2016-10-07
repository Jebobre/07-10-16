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
        random_noise=random.uniform(0,step)
        new_value=idx*step+random_noise
    else:
        new_value = idx*step
    return new_value

def values_equalization(values,percentiles,add_random=False):
    for i in range(len(values)):
        values[i]=value_equalization(values[i],percentiles,add_random)
    return values


file_input=open('img.txt','r')
data=[]
s=file_input.readline()
while len(s)>0:
    s=s.rstrip()
    C=list(map(float,s.split(' ')))
    data.append(C)
    s=file_input.readline()

data=np.array(data)

plt.subplot(222)

plt.hist(data.flatten(),bins=10)

plt.subplot(221)

plt.imshow(data,cmap=plt.get_cmap('gray'))

data=data.flatten()
data=values_equalization(data,get_percentile(data,250))
data=np.array(data)
data=data.reshape((200,267))

plt.subplot(224)

plt.hist(data.flatten(),bins=10)

plt.subplot(223)

plt.imshow(data,cmap=plt.get_cmap('gray'))

plt.show()