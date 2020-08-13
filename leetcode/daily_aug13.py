
'''
Iterators for combination. Tags:
<T> Backtracking, <T> Recursion


Just gonna use the itertools for daily submit,
todo return for the other implementation later


'''

from itertools import combinations

class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        #r-length tuples, in sorted order, no repeated elements
        # https://docs.python.org/2/library/itertools.html
        self.comb_arr = []
        for comb in combinations(characters, combinationLength):
            self.comb_arr.append(comb)
        
        self.curr_item = 0

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.curr_item += 1
            return "".join(self.comb_arr[self.curr_item-1])
        else:
            return None
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curr_item < len(self.comb_arr):
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()