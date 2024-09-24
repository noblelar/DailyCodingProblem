

# ! Problem 1

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def two_sums( nums, k):
   seen = set()
   for num in nums:
      if k - num in seen:
         return True
      seen.add(num)

   return False


nums = [10, 15, 3, 7]
k = 17
print(two_sums(nums, k))

 
# ! Problem 2

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


def productExceptSelf (nums):
   n = len(nums)
   leftProduct = [1 for _ in range(n)]
   rightProduct = [1] * n
   result = [1 for _ in range(n)]

   for i in range(1, n):
        leftProduct[i] = leftProduct[i - 1] * nums[i - 1] 

   for i in range(n - 2, -1, -1):
        rightProduct[i] = rightProduct[i + 1] * nums[i + 1]

   # print(leftProduct)
   # print(rightProduct)

   for i in range(n):
        result[i] = leftProduct[i] * rightProduct[i]

   return result


#  Example usage
nums1 = [1, 2, 3, 4, 5]
print(productExceptSelf(nums1))