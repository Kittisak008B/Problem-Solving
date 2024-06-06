# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

# Example 1:
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

# Example 2:
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0 :
            return False
        d = defaultdict(int)
        for card in hand :
            if card not in d :
                d[card] = 0
            d[card] += 1
        heap = list(d.keys())
        heapq.heapify(heap)
        while heap :
            min_card = heap[0]
            for card in range(min_card , min_card + groupSize) :
                if card not in d :
                    return False
                d[card] -= 1
                if d[card] == 0 :
                    heapq.heappop(heap)
        return True

# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand) % groupSize != 0 :
#             return False
#         d = defaultdict(int)
#         for card in hand :
#             if card not in d :
#                 d[card] = 0
#             d[card] += 1
#         sort_d = sorted(d.keys())
#         for card in sort_d :
#             if d[card] > 0 :
#                 for i in range(1 , groupSize) :
#                     if d[card + i] < d[card] :
#                         return False
#                     d[card + i] -= d[card]
#         return True
