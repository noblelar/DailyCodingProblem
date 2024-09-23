

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

