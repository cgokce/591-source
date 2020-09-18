'''
Calculate the h-index value

"A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

we can randomly select h, between 1-paper_count

Look for papers have h+ citations
N = arr[i > h]

if N < h:
    # Need to reduce h
if N >= h:
    # Check if h+1 does same
    # If not, h-index is true


Not working bad approach
def hIndex(self, citations: List[int]) -> int:

# Check the given h index is valid
def check_if_valid(h, array, processed):
    n = 0
    for item in array:
        if item >= h:
            n += 1 

    n += processed
    print("n . ", n, " h. ", h)
    if n>=h:
        return 1
    else:   
        return 0

# Unit test
#print(check_if_valid(3, citations))

def dfs(citations, processed):

    # Base case
    if len(citations) == 1:
        if citations[0] == 1:
            return 1
        else:
            return 0
    elif len(citations) == 0:
        print("base case with", citations)
        return 0


    # Sample the random val check h is valid
    total_papers = len(citations)

    index = random.randint(0, total_papers-1)
    #print("index ", index, citations)

    h = citations[index]

    print("h: ",h, " ", citations)

    if check_if_valid(h, citations, processed):
        print("valid, check bigger")
        # Bigger: Check just the bigger array 


        # todo, this can also be done with one-liner

        return h + dfs([item for item in citations[index+1:]][:],0)

    else:
        print("invalid, check smaller")
        # THIS IS WRONG
        # Get the smaller h but you only need a bigger array
        # You don't even need to reiterate
        # It can be done w one liner
        for k in range(index-1, -1, -1):
            # Not processed length + k
            threshold = len(citations) - index +k
            if k >= threshold:
                return k
            else: 
                return 0
        #return max(processed, dfs([item for item in citations[:index]][:], h))


# Sort the arr beforehand
arr_sorted = sorted(citations)

print(arr_sorted)

return dfs(arr_sorted,0)

[3,0,6,1,5]
Output:
1
Expected:
3
Stdout:
[0, 1, 3, 5, 6]
h:  1   [0, 1, 3, 5, 6]
valid, check bigger
h:  3   [3, 5, 6]
invalid, check smaller
base case with []
'''

'''
def hIndex(self, citations: List[int]) -> int:
arr_sorted = sorted(citations)
print(arr_sorted)

prev_valid = -1

if arr_sorted == []:
    return 0
if len(arr_sorted)==1:
    if arr_sorted[0]>=1:
        return 1
    else:
        return 0

prev_h = -1

# Only increment, use double 
for i in range(len(arr_sorted)):

    if i+1 == len(arr_sorted):
        h = arr_sorted[i]
        if h == 0:
            return 0
        if h == 1:
            return 1
        else:
            return prev_h

    h = arr_sorted[i]
    h2 = arr_sorted[i+1]
    print(h,h2)

    # How many remaining items?
    remaining = len(arr_sorted)-i
    print("remain ", remaining)

    if remaining-1 >= h:
        print("skip,increment")
        if h >=remaining:
            prev_h = remaining
        else:
            prev_h = h
        continue
    elif remaining >= h:
        print("settle")
        for i in range(h2-1, h-1,-1):
            print("traversing")
            if remaining >= i :
                return i
    else:
        print("else")
[0,0]


[0,1]

[11,15]

[1,2]
'''


class Solution:
    
    def hIndex(self, citations: List[int]) -> int:
        arr_sorted = sorted(citations)
        #print(arr_sorted)
        size = len(citations)
        i= 1
        
        while i <= size:
            #print(i)
            if(arr_sorted[size-i] < i):
                break
            i+=1
                
        return i-1
    
