'''

find(s,w, prev):
start string s
iterate word dict -> w
if s starts with w
    keep the prev processed part -> prev
    repeat s-w, dict-w, prev + " " + w


Samples

abc
-> [a,b,c]
ret: ["a b c"]

Still have the time limit error, needs a DP solution
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        return self.dfs(s, wordDict, "")
        
    # Default call ("", wordDict list)
    def dfs(self, curr_string, wordDict, prefix):
        outList = []
        exists = False
        multi_success = False

        # Use the find method, it returns zero if match is at beginning.
        for item in wordDict:
            #print("str", curr_string)
            #print(item)
            #if curr_string == "aaaaaaa":
            print("1-", curr_string)
            print("2-", item)
            print("---")

            if curr_string.find(item) == 0:           
                #print(curr_string[curr_string.find(item) + len(item):]) 
                '''
                print("1-", curr_string)
                print("2-", item)
                print("---")
                '''
                if prefix == "":
                    updated_prefix = item
                else:
                    updated_prefix = prefix + " " + item
                
                if len(item) == len(curr_string):

                    # Can have multiple success cases here. 
                    multi_success = True
                    outList.append(updated_prefix)

                    # Success -Single - Still alternatives exists
                    #return updated_prefix
                else:
                    # Branch and Stack
                    exists = True
                    ret = self.dfs(curr_string[curr_string.find(item) + len(item):], wordDict, updated_prefix) 
                    if len(ret) > 0:
                        # Change this to unicode in the leetcode editor
                        if isinstance(ret, str):
                            outList.append(ret)
                        else:
                            outList.extend(ret)
                        

        # Failure Single
        if multi_success == True:
            return outList
        elif exists == False:
            return ""
        else: # Success TOtal
            return outList


solution = Solution()
#s = "catsandog"
#wordDict = ["cats", "dog", "sand", "and", "cat"]

#s = "pineapplepenapple"
#wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

#s = "catsanddog"
#wordDict = ["cat","cats","and","sand","dog"]

#s = "pineapplepenapple"
#wordDict = ["apple","pen","applepen","pine","pineapple"]

s = "aaaaaaa"
wordDict = ["aaaa","aa","a"]

outList = solution.wordBreak(s, wordDict)

print("######")

print(outList)

for i in outList:
    print(i)
