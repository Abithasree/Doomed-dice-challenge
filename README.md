# Doomed-dice-challenge

# Securin-assessment

## Part A

### Question 1:

To calculate the total number of combinations possible when rolling two six-sided dice, you multiply the number of faces on each die.

Mathematically, it can be expressed as:

Total combinations = Number of faces on Die 1 × Number of faces on Die 2

In this case:
- Number of faces on Die 1 = 6
- Number of faces on Die 2 = 6

So, the total number of combinations is:
Total combinations = 6 × 6 = 36

![Screenshot 2024-03-24 023052](https://github.com/Abithasree/Doomed-dice-challenge/assets/109432119/fdd7a76a-1f00-40dd-9e5b-84c432ea8996)

### Question 2:

To calculate and display the distribution of all possible combinations that can be obtained when rolling both Die 1 and Die 2 together, we'll create a 6x6 matrix representing all possible combinations.


![Screenshot 2024-03-24 023113](https://github.com/Abithasree/Doomed-dice-challenge/assets/109432119/da54af7d-a592-4846-b52a-255b03c8b780)

We represent the distribution as a 6x6 matrix where each cell (i, j) represents the combination obtained by rolling Die 1 and Die 2, respectively.

### Question 3:

To calculate the probability of all possible sums occurring among the number of combinations from Question 2, we can use the formula:

P(sum=x) = number of times x appeared / total number of outcomes

![Screenshot 2024-03-24 023156](https://github.com/Abithasree/Doomed-dice-challenge/assets/109432119/eca21825-50d6-4640-b7f3-f5dd892c1628)


## Part B

## Undooming the Dice Algorithm

### Overview
This algorithm is designed to adjust the values of two dice to match the original probabilities of their sums, while avoiding any occurrences of zero. The process involves determining the minimum and maximum occurrences for one of the dice based on the original probabilities, and then iteratively adjusting the values of both dice until the desired probabilities are achieved.

### Steps
1. **Original Probabilities Calculation**:
   - Calculate the probabilities of all possible sums of two dice rolls.

2. **Undooming the Dice**:
   - Initialize new dice values with zeros.
   - Assign minimum values to the first four positions of new_dice1.
   - Generate new_dice2 by replacing zeros with values not present in new_dice1.

3. **Determining Must Occurrences for new_dice2**:
   - Identify sum values with exactly one occurrence in the original counts.
   - Determine the maximum must occurence and minimum must occurrence values for new_dice2 based on these unique sum values i.e 2 and 12.

4. **Assigning Values to new_dice2**:
   - Replace zeros in new_dice2 with the determined maximum and minimum occurrences.

5. **Brute-force Replacement**:
   - Iterate over all possible combinations of the last two positions in both new_dice1 and new_dice2. (i.e we are replacing the rermaining zeroes)
   - Check if the probabilities match the original probabilities.
   - If a match is found, display the combination.

### Usage
To use this algorithm:
1. Provide the original dice values and the number of faces.
2. Run the algorithm to obtain adjusted dice values that match the original probabilities.

### Example
For a demonstration of how to use this algorithm, refer to the provided code examples and explanations. :)
     
![Screenshot 2024-03-24 023259](https://github.com/Abithasree/Doomed-dice-challenge/assets/109432119/1ee00529-6fd7-42f9-b389-43bd8d22c4ad)

By following this approach, we ensure that the probabilities of obtaining sums remain unchanged while reattaching spots to the dice, thus satisfying the conditions imposed by Loki.


