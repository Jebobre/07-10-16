__author__ = 'student'
import random
import matplotlib.pyplot as plt
import numpy as np

file_input=open('img.txt','r')
data[]
s=file_input.readline()
while len(s)>0:
    s=s.rstrip()
    C=list(map(float,s.split(' ')))
    data.append(C)
    s=file_input.readline()

data=np.array(data)

plt.figure(1)
plt.hist(data.flatten(),bins=10)
