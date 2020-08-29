Backtracking
- Topics: Subsets, Permutations, Combinations
- Great overview on this [link](https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning))

Python Notes
- Set operations are available, eg. diff, union...
- Permutation and combinations are available using itertools

        myList = [3,4,5]
        // return subsets with the given size
        itertools.combinations(myList, subsetSize)
        // same for the permutations
        itertools.permutations(myList, subsetSize)