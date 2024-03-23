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

To solve the problem of reattaching spots to the dice while maintaining the same probabilities of obtaining sums, I followed a systematic approach. Here's a concise summary of the logic and approach:

1. **Initial Setup:**
   - We start with Die 1 having values [1, 2, 3, 4, 0, 0] and Die 2 having values [1, 5, 6, 8, 0, 0].
   - Die 1 has zeros for the last two faces because it cannot have more than 4 spots, and Die 2 includes values beyond 4 to accommodate missing 5 and 6 from die 1.

2. **Calculate Original Probabilities:**
   - We calculate the probabilities of all possible sums when rolling both dice together.
   - This is done by enumerating all combinations and counting the occurrences of each sum.

3. **Check for Consistency:**
   - We define a function `check_okay()` to compare the probabilities of sums with the original probabilities.
   - If the probabilities match, it indicates that the reattached spots maintain the same probabilities.

4. **Brute-Force Approach:**
   - We use a brute-force approach to find valid spot combinations for the remaining zeros on Die 1 and Die 2.
   - We iterate over all possible combinations for the remaining spots, keeping in mind the constraints on the dice.

5. **Output the Solution:**
   - Once a valid combination is found, we output the final configurations of Die 1 and Die 2.
     
![Screenshot 2024-03-24 023259](https://github.com/Abithasree/Doomed-dice-challenge/assets/109432119/1ee00529-6fd7-42f9-b389-43bd8d22c4ad)

By following this approach, we ensure that the probabilities of obtaining sums remain unchanged while reattaching spots to the dice, thus satisfying the conditions imposed by Loki.


