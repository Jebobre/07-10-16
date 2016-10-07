__author__ = 'student'
import random
import matplotlib.pyplot as plt

random.seed(0)
n=1000000
sum=0
for i in range(n):
    x=random.uniform(-3,3)
    if x>=-2 and x<=2:
        x=-x**2+4
    else:
        x=0
    sum+=x

plt.show()
print(6/n*sum)