import numpy as np

# Original dice values
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

# Calculate sum of all combinations
sums = np.zeros((6, 6), dtype=int)
for i in range(6):
    for j in range(6):
        sums[i][j] = dice1[i] + dice2[j]

probabilities = {}
counts = {}
for sum_val in range(2, 13):
    count = np.count_nonzero(sums == sum_val)
    counts[sum_val] = count
    probabilities[sum_val] = count / 36

print("\nOriginal probabilities:", probabilities)
print("Original counts:", counts)

new_dice1 = [1, 2, 3, 4, 0, 0]
new_dice2 = [1, 5, 6, 8, 0, 0]

def check_okay():
    new_sums = np.zeros((len(new_dice1), len(new_dice2)), dtype=int)
    for i in range(len(new_dice1)):
        for j in range(len(new_dice2)):
            new_sums[i][j] = new_dice1[i] + new_dice2[j]

    new_probabilities = {}
    for sum_val in range(2, 13):
        count = np.count_nonzero(new_sums == sum_val)
        new_probabilities[sum_val] = count / (len(new_dice1) * len(new_dice2))
    if new_probabilities == probabilities:
        print("\nnew probabilities: ",new_probabilities)
        return True
    return False

#brute-force
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 12):
            for l in range(1, 12):
                new_dice1[4] = i
                new_dice1[5] = j
                new_dice2[4] = k
                new_dice2[5] = l
                if check_okay():
                    print("\nFound combination:")
                    print("Dice1:", new_dice1)
                    print("Dice2:", new_dice2)
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break
