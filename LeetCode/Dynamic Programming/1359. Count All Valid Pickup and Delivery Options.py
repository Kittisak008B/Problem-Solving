# Given n orders, each order consists of a pickup and a delivery service.
# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
# Since the answer may be too large, return it modulo 10^9 + 7.

# Example 1:
# Input: n = 1
# Output: 1
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
  
# Example 2:
# Input: n = 2
# Output: 6
# Explanation: All possible orders: 
# (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
# This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

# Example 3:
# Input: n = 3
# Output: 90
 
# Constraints:  1 <= n <= 500

class Solution:
    def countOrders(self, n: int) -> int:
        dp = {}
        def dfs(pickups_remain , order_toDelivery) :
            if pickups_remain < 0 or order_toDelivery < 0 :
                return 0
            if pickups_remain == 0 and order_toDelivery == 0 :
                return 1
            if (pickups_remain , order_toDelivery) in dp :
                return dp[(pickups_remain , order_toDelivery)]

            ways = 0
            if pickups_remain > 0 :
                ways += dfs(pickups_remain -1 , order_toDelivery +1) *pickups_remain
            if order_toDelivery > 0 :
                    ways += dfs(pickups_remain , order_toDelivery -1) *order_toDelivery

            dp[(pickups_remain , order_toDelivery)] = ways
            return dp[(pickups_remain , order_toDelivery)]
        return dfs(n , 0) % (10**9 + 7)
'''
n = 2
        (pickups_remain , order_toDelivery)
               _____(n , 0)_______
              /      (2,0)        \ 
            P1                    P2
           (1,1) 
           /   \                  /  \
          P2    D1               P1   D2
        (0,2)  (1,0)  
         / \     \                /\     \ 
        D1  D2   P2              D2 D1    P1
     (0,1)(0,1)  (0,1)   
       /     \     \             /   \      \
      D2      D1   D2           D1    D2     D1
   (0,0)    (0,0) (0,0)
   way+1   way+1  way+1   
            
            dp = {(0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 3, (2, 0): 6}
'''
