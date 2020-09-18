'''

Distribute Candies to People
<T> Math
 
Distribute candies to the people (n)

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

- 1,2...n candies for each person
then go to start
- n+1,n+1....2*n

we repeat the process
until no more candies left


return arr:<int> final dist of candies
unit: len(num_people) sum(candies)

algorithm: 
- since candies are provided sequentially we calc the math result of it

        we calculate math eq
        1 + .... n  = n (n+1) / 2  -- True formula
        n(1) = 1
        n(0) = 0
        1 + 2 = 3   2 * 3 / 2  = 3 

def get_series(n):
    if n<=1:
        return n
    else:
        return (n * (n-1))/2


we have given = series(n) + k 
we can calculate array beforehand, and lets do it recursively


def calc_n(res):
    n, series = 0, 0

    while(series<res):
        n += 1
        series = get_series(n)            
    return n-1
    

    
# We have calculated the n at this point
# Lets calculate the array

out_arr = []

1     2   3 ... n
n+1 n+2
2n + 1

1 + n+1 + 2n+1 + ....

series(k)
1*k + (0 + 1 .+ k-1) *n = k + (k-1) *n 


k + (k-1) *n

This is getting out of hand, lets do the brute force first



'''

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        
        
        out_arr = [0 for i in range(num_people)]
        curr_series = 0
        final = False
        while ( candies > 0 ):       
            for i in range(num_people):
                curr_series += 1
                if candies - curr_series>=0:
                    # Feasible to distribute
                    candies = candies - curr_series
                    out_arr[i] += curr_series
                else:
                    # Final addition
                    final = True
                    out_arr[i] += candies
                    break
                    
            if final:
                break

        return out_arr
        
        