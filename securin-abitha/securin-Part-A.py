import time
import random
import numpy as np

dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]

# Part-A question 1.

print("possible values from dice 1:" ,6)
print("possible values from dice 2:" ,6)
tot_comb=6*6
print("total possible combinations is 6*6= ",tot_comb)


# Question 2.

print("\npossible combinations for two dice\n")


distribution = np.zeros((6, 6), dtype=object)

for i,k in enumerate(dice1):
    for j,l in enumerate(dice2):
        distribution[i][j] = (k,l)

print("Distribution of all possible combinations:")
print(distribution,"\n")


# Question 3

dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
sum= np.zeros((6,6), dtype=object)
for i in range(6):
    for j in range(6):
        sum[i][j]=dice1[i]+dice2[j]
print(sum)

for sum_val in range(2,13):
    count= np.count_nonzero(sum==sum_val)
            
    print(f"Probability of Sum = {sum_val}: {count/tot_comb}")
    count=0
