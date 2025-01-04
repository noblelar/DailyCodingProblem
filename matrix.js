function maxCoins(matrix) {
   const rows = matrix.length;
   const cols = matrix[0].length;

   // Create a DP table
   const dp = Array.from({ length: rows }, () => Array(cols).fill(0));

   // Initialize the first cell
   dp[0][0] = matrix[0][0];

   // Fill the first row
   for (let j = 1; j < cols; j++) {
       dp[0][j] = dp[0][j - 1] + matrix[0][j];
   }

   // Fill the first column
   for (let i = 1; i < rows; i++) {
       dp[i][0] = dp[i - 1][0] + matrix[i][0];
   }

   // Fill the rest of the dp table
   for (let i = 1; i < rows; i++) {
       for (let j = 1; j < cols; j++) {
           dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j];
       }
   }

   // Return the value in the bottom-right corner
   return dp[rows - 1][cols - 1];
}

// Test case
const matrix = [
   [0, 3, 1, 1],
   [2, 0, 0, 4],
   [1, 5, 3, 1]
];

console.log(maxCoins(matrix)); // Output: 12
