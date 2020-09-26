'''
Teemo Attacking

Array -> arr : timeseries -> times of attack
        int: duration  -> duration of poison
        
O(n)
- linearly iterate

ret = 0
- each unit
    - if curr_time - prev_time < duration:
        prev_time = curr_time
        ret += curr_time - prev_time
      

'''

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        if timeSeries == []:
            return 0
        
        ret = 0
        for i in range(len(timeSeries) -1):
            
            # Final element
            curr_time = timeSeries[i+1]
            prev_time = timeSeries[i]
            #print("-- Curr: ", curr_time, " Previous: ", prev_time)
            
            # and (i != len(timeSeries) -1 )
            # poisoned
            if (curr_time - prev_time < duration):
                ret += curr_time - prev_time
            else:
                ret += duration
         
            
        return ret + duration
            