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
