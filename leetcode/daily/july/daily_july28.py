'''
Task list array.
Obj: return the most efficient array size

Constraints
---> Each day 1 task or idle
---> n denotes time limit for returning the same task 
    --> A -> n day idle -> A again
    
Algorithm
(simple greedy approach)
def algo(tasks, n):
    
    # We can go with greedy algorithm
    # To priotrioze task with its count
    # Since it'll solve the selection problem
    
    # Counts
    counts = {}
    
    for item in n:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 0
    
    
    # Start by greedy addition
    # Need to sort dictionary with the highest val to lowest
    sorted = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}
    keys = sorted.keys():
    cooldowns = [0 for i in range(len(keys))]
    days = 0
    
    for i in range(len(tasks)):
    
    
        # Select a greedy key without a cd
        for i in range len(keys):
            k = keys[i]
            v = sorted[k]
            cd = cooldowns[i]
            # If task needed & no cooldown
            if v>0 and cd == 0:
                sorted[k] -= 1
                cooldowns[i] = n
    
        # Reduce all cooldowns by 1
        cooldowns = [max(0, i-1) for i in cooldowns]
        days += 1


    return days

'''



class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        #tasks = ["A","B","C","A","B"]
        #n = 2
        
        # Counts
        counts = {}

        for item in tasks:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1


        #counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
        keys = [k for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)]
        cooldowns = [0 for i in range(len(keys))]
        days = 0

        
        #for k in keys:
        #    print(k, counts[k])
        
        assigned = 0
        while(assigned<len(tasks)):
            # Shuffle the keys
            #keys = [k for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)]
            for i in range(len(keys)):
                k = keys[i]
                v = counts[k]
                cd = cooldowns[i]
                # If task needed & no cooldown
                if v>0 and cd <= 0:
                    counts[k] -= 1
                    cooldowns[i] = n+1
                    assigned += 1
                    #print(k)
                    break

            cooldowns = [max(0, i-1) for i in cooldowns]
            days += 1

        return days
        
#tasks = ["A","B","C","A","B"]
#n = 2
#out: 6
#expect: 5

#tasks = ["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"]
#n = 2