def max_coins(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a DP table
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the first cell
    dp[0][0] = matrix[0][0]

    # Fill the first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    # Fill the first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    # Fill the rest of the dp table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    # Return the value in the bottom-right corner
    return dp[rows - 1][cols - 1]

# Test case
matrix = [
    [0, 3, 1, 1],
    [2, 0, 0, 4],
    [1, 5, 3, 1]
]

print(max_coins(matrix))  # Output: 12
