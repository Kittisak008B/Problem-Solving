# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. 
# Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.
# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
# Given the integer array position and the integer m. Return the required force.

# Example 1:
# Input: position = [1,2,3,4,7], m = 3
# Output: 3
# Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. 
# We cannot achieve a larger minimum magnetic force than 3.
  
# Example 2:
# Input: position = [5,4,3,2,1,1000000000], m = 2
# Output: 999999999
# Explanation: We can use baskets 1 and 1000000000.
 
# Constraints:  1 <= position[i] <= 109    All integers in position are distinct.    2 <= m <= position.length

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def ballplaced(force) :
            prev = position[0]
            num_ballplaced = 1
            for i in range(1 , len(position)) :
                if position[i] - prev >= force :
                    num_ballplaced += 1
                    prev = position[i]
            return num_ballplaced
        position.sort()
        l , r = 1 , position[-1]
        force = 1
        while l <= r :
            mid = l+(r-l)//2
            if ballplaced(mid) >= m : #can place m ball -> increase force
                force = mid
                l = mid + 1
            else :    #can't place m ball -> decrease force
                r = mid - 1
        return force
'''
max force(distance) to place m balls
position = [1,2,3,4,7], m = 3

serch range (force) ->[1 , 7]  -> force = (1+7)//2 = 4

            [1,2,3,4,7]
             x       x  cant place 3 ball -> decrease force -> force = (1+3)//2 = 2
            [1,2,3,4,7]
             x   x   x  can place 3 ball  -> increase force -> force = (3+3)//2 = 3
            [1,2,3,4,7]
             x     x x      out of loop -> return force = 3 
'''
