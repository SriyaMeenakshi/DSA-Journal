"""An array nums will be given, we need to find the contiguous subarray which has the largest sum.
We need to return the sum of that subarray.
We can do this by taking two for loops and checking subarrays with each element,but it takes O(n^2) time complexity. We can do this in O(n) time complexity using Kadane's algorithm."""
"""Kadane's algorithm we traverse in single pass
We keep track of previous element max sum.
We add prev_elem_max_sum to current element
i) If the sum is positive we update prev_elem_max_sum=prev_elem_max_sum+current element
ii) If the sum is negative we update prev_elem_max_sum=current element.
We update main_sum=max(main_sum,prev_elem_max_sum)
"""
def maxSubarraySum(arr):
    
    main_sum=arr[0] #2
    prev_elem_max_sum=arr[0] #2
    for i in range(1,len(arr)):
        prev_elem_max_sum=max(prev_elem_max_sum+arr[i],arr[i]) #steps 1 and 2
        #ps=(2+3,3)=5
        #ps=(5-8,-8)=-3
        #ps=(-3,7)=7 #new subarray is taken from this element
        #ps=(7-1,-1)=6
        #ps=(6+2,2)=8
        #ps=(8+3,3)=11
        main_sum=max(main_sum,prev_elem_max_sum)
        #ms=(2,5)=5
        #ms=(5,-3)=5
        #ms=(5,7)=7
        #ms=(6,7)=7 #the sum is not updated so only one element will be taken if array stops
        #ms=(7,8)=8
        #ms=(8,11)=11 #loop ends
    return main_sum #11 is returned



if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(maxSubarraySum(arr))