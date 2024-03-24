import numpy as np

# Original dice values
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
faces = 6

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

# Checking if probabilities match or not
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
        print("\nNew probabilities:", new_probabilities)
        return True
    return False

# Brute-force to find combination of dice values
def brute_force_zeroes(new_dice1, new_dice2):
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
                        return
                    else:
                        print("\nTried combination:")
                        print("Dice1:", new_dice1)
                        print("Dice2:", new_dice2)

# Undooming the dice
def undoom_dice():
    global new_dice1, new_dice2

    # Append all minimum values to dice1 having constraint < 5
    for i, j in enumerate(range(1, 5)):
        new_dice1[i] = j
    
    # We are done with dice1! (for now)
    
    # Generate new_dice2 by replacing values of zero with values not present in dice1 1. let other values be 0
    new_dice2 = [x if x not in new_dice1 else 0 for x in range(6, 0, -1)]

    # Now check the count probabilities which equal exactly 1; these values hold the MUST occurrences in dice2
    keys_with_value_one = [key for key, value in counts.items() if value == 1]
    max_occurrence_for_dice2 = max(keys_with_value_one) - max(new_dice1)
    non_zero_values = [x for x in new_dice1 if x != 0]
    min_occurrence_for_dice2 = min(keys_with_value_one) - min(non_zero_values)
    
    # Iterate through new_dice2 and replace zeroes with max_occurrence_for_dice2 and min_occurrence_for_dice2
    for i in range(len(new_dice2)):
        if new_dice2[i] == 0:
            if new_dice2[i + 1] == 0:
                new_dice2[i] = max_occurrence_for_dice2
                new_dice2[i + 1] = min_occurrence_for_dice2
                break

    # All done! Now apply brute force to check to replace remaining zeroes in new_dice1 and new_dice2
    brute_force_zeroes(new_dice1, new_dice2)

# Initialize new dice values
new_dice1 = [0] * 6
new_dice2 = [0] * 6

# Call function to undoom the dice
undoom_dice()
