# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
# Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

# Example 2:
# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]
 
# Constraints:
# All the elements of arr2 are distinct.
# Each arr2[i] is in arr1.

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hm_arr1 = defaultdict(int)
        arr2_set = set(arr2)
        remain_arr1 = []
        for x in arr1 :
            if x not in arr2_set :
                remain_arr1.append(x)
            else :
                hm_arr1[x] += 1 
        remain_arr1 = sorted(remain_arr1)
        ans = []
        for x in arr2 :
            while hm_arr1[x] > 0 :
                ans.append(x)
                hm_arr1[x] -= 1
        for x in remain_arr1 :
            ans.append(x)
        return ans 
