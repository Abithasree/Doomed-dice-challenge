"""PART A"""
import time
import random
import numpy as np
print("lets role two dice!")
print("rolling...")
time.sleep(2)
dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
print("Dice1: ",dice1[random.randint(0,5)])
print("Dice2: ",dice2[random.randint(0,5)])
time.sleep(1)

# Part-A question 1.

"""The total combinations possible when rolling two six-sided dice 
can be calculated by multiplying the number of faces on each die"""

print("\nyou can see the above two dice gives random values between range of 1 and 6!\nnow lets see how many combinations\n ")
time.sleep(2.5)
print("possible values from dice 1:" ,6)
print("possible values from dice 2:" ,6)
tot_comb=6*6
print("total possible combinations is 6*6= ",tot_comb)
time.sleep(4.5)

# Question 2.

print("\nso how many possible combinations for two dice?")
time.sleep(2)
print("\nlets see!")
print("calculating...\n")
time.sleep(2.5)

distribution = np.zeros((6, 6), dtype=object)

for i,k in enumerate(dice1):
    for j,l in enumerate(dice2):
        distribution[i][j] = (k,l)

print("Distribution of all possible combinations:")
print(distribution,"\n")
time.sleep(3)

# Question 3

"""Calculating the Probability of all Possible Sums occurring among the number of
combinations from (2)"""

""" formula : P(sum=x)= no.of times X appeared/ total no.of outcomes"""
dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
sum= np.zeros((6,6), dtype=object)
for i in range(6):
    for j in range(6):
        sum[i][j]=dice1[i]+dice2[j]
print(sum)
"""now sum of two dice are stored in matrix lets see probability for each sum"""
for sum_val in range(2,13):
    count= np.count_nonzero(sum==sum_val)
            
    print(f"Probability of Sum = {sum_val}: {count/tot_comb:.2f}")
    count=0
        


