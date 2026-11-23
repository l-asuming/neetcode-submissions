class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        i = 1
        j = max(piles)
        
        min_rate = max(piles)
      

        notfound = True

        while i < j:
            k = (i + j)//2
        
            time_list = [(p+k-1)//k for p in piles]
            total_time = sum(time_list)
            
            if total_time <= h:
                min_rate = min(min_rate,k)
                j = k
        
            else:
                i = k+1
        
        return min_rate
            
            