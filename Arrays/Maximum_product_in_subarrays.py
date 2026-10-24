""" Maximum Product Subarray in an Array
Given an integer array nums. Find the subarray with the largest product, and return the product of the elements present in that subarray.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [4, 5, 3, 7, 1, 2]

Output: 840

Explanation:

The largest product is given by the whole array itself
"""



def maxProduct( nums: list[int]) -> int:
    n=len(nums)
    curr_min=nums[0]
    curr_max=nums[0]
    max_product=nums[0]
    if len(nums)==0:
        return 0
        
    for i in range(1,n):
        curr_value=nums[i]
        prev_max=curr_max
        prev_min=curr_min
        curr_max=max(
                curr_value,
                prev_max*curr_value,
                prev_min*curr_value
            )
        curr_min=min(
                curr_value,
                prev_max*curr_value,
                prev_min*curr_value
                )
        if curr_max>max_product:
            max_product=curr_max
            
    return max_product

if __name__ == "__main__":
    nums = [2, 3, -8, 7, -1, 2, 3]
    print(maxProduct(nums))
