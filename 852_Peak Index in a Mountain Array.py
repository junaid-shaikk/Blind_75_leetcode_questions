''' Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
 

Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array. '''

#CODE

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maximum=arr[0]
        c=0
        for i in range(1,len(arr)):
            if arr[i]>maximum:
                maximum=arr[i]
                c+=1
        return c
      
        #or
        
        '''
        return arr.index(max(arr))
        '''
