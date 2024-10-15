console.log("Let's begin");

// ! Problem 1

// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

function sum_check(nums, k) {
  const seen = new Set();

  for (let num of nums) {
    if (seen.has(k - num)) {
      return true;
    }
    seen.add(num);
  }

  return false;
}

// ? Test examples

const nums = [10, 15, 3, 7];
const k = 17;
console.log(sum_check(nums, k));

//  ! Problem 2

// Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

// For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

// Follow-up: what if you can't use division?

// ? SOLUTION 1 {O(N^2)}

function multiply(nums) {
  let ans = 1;
  nums.map((num) => {
    ans *= num;
  });
  return ans;
}

function create_array(nums) {
  let original_array = [...nums];
  const soln = [];
  for (let i = 0; i < original_array.length; i++) {
    let clone = [...original_array];
    clone[i] = 1;
    soln.push(multiply(clone));
  }
  return soln;
}

// ? WITH DIVISION 



// ? SOLUTION 2 {O(N)}
function productExceptSelf(nums) {
  const n = nums.length;
  const leftProducts = new Array(n).fill(1);
  const rightProducts = new Array(n).fill(1);
  const result = new Array(n);

  // Build the left products array
  for (let i = 1; i < n; i++) {
    leftProducts[i] = leftProducts[i - 1] * nums[i - 1];
  }

  // Build the right products array
  for (let i = n - 2; i >= 0; i--) {
    rightProducts[i] = rightProducts[i + 1] * nums[i + 1];
  }
  console.log(leftProducts);
  console.log(rightProducts);

  // Construct the result by multiplying left and right products
  for (let i = 0; i < n; i++) {
    result[i] = leftProducts[i] * rightProducts[i];
  }

  return result;
}

// Example usage
const nums1 = [1, 2, 3, 4, 5];
console.log(productExceptSelf(nums1)); // Output: [120, 60, 40, 30, 24]

const test1 = [1, 2, 3, 4, 5];
console.log(create_array(test1));


