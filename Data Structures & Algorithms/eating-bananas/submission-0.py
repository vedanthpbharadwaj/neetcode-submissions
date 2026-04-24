class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1 # lowest speed (0 is impossible)
        high = max(piles) # fastest possible speed of Koko eating bananas
        answer = high # best valid answer found so far

        while low <= high:
            mid = (low + high) // 2

            total_hours = 0

            for pile in piles: # going through all the piles 
                total_hours += (pile + mid - 1)//mid  # same as ceil(pile//mid) just integer math is faster

            if total_hours <= h:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer

