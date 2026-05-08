class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate = 1
        maxRate = max(piles)

        res = max(piles)

        while minRate <= maxRate:
            midRate = (minRate + maxRate) // 2
            totalHours = 0
            for pile in piles:
                hoursToEat = math.ceil(pile / midRate)
                totalHours += hoursToEat
            if totalHours <= h:
                res = midRate
                # search lower rates (left)
                maxRate = midRate - 1
            else:
                # search lower rates (left)
                minRate = midRate + 1
        return res