# Task Description: Complete the following tasks.

# Task-1:  Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
# or false otherwise. In other words, return true if one of s1's permutations 
# is the substring of s2.

# s="acb"

#find all permuations of s  n->len(s)
#dfs
#time O(n*n!) factorial space O(n * n!)  average length of each permutation times result
#_,_,_,_ 
def permutation(s):
    res = []
    def dfs(visited, cur):
        #exit condition
        if len(visited) == len(s):
            res.append(cur)
            return
        for idx in range(len(s)):
            if idx in visited:
                continue
            visited.add(idx)
            dfs(visited, cur+s[idx])
            #other function call can use
            visited.remove(idx)
    dfs(set(), "")
    return res

def isPermutation(s1, s2):
    allP = permutation(s1)
    for p in allP:
        if p in s2:
            return True
    return False


# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# Write sample test cases to validate your implementation.
# Task-2:  You are given a chess board (of 8×8 dimension), and there are 8 queens placed randomly on the board. 
# Each of the 8 queens is in different columns, and that means no two queens are attacking each other vertically. 
# But some queens are attacking each other horizontally and/or diagonally. 
# You have to move the queens so that no two queens are attacking each other from any direction. 
# You are allowed to move the queens vertically, and thus, 
# you can only change the row positions of each queen and not the column. 
# A move consists of moving a queen from (R1, C) to (R2, C) where 1 ≤ R1, R2 ≤ 8 and R1 ̸= R2. 
# You have to find the minimum number of moves required to complete the task.
# Each input consists of a line containing 8 integers. 
# All these integers will be in the range [1, 8]. 
# The i-th integer indicates the row position of a queen in the i-th column.
# Example 1: 
# Input: 1 2 3 4 5 6 7 8
# Output: 7
# Example 2:
# Input: 1 1 1 1 1 1 1 1
# Output: 7
# Write sample test cases to validate your implementation.
# queens = [1 2 3 4 5 6 7 8]
#          [1 ]

#time O(n!) n factorial  n*(n-1)*(n-2)...*1
#space O(n)
def minMoves(queens):
    #set first value to infinite
    curMin = float('inf')

    usedRows = set()
    #minus two points have the same row minus/plus col  they are on a diagonal line
    diag1 = set()
    #plus  diagonal
    diag2 = set()

    def backtrack(col, curSteps):
        nonlocal curMin
        #exit condition
        if col == 8:
            curMin = min(curMin, curSteps)
            return

        #early stop /prune impossible cases
        if curSteps >= curMin:
            return

        for row in range(1,9):
            if row in usedRows:
                continue
            if row-col in diag1:
                continue
            if row+col in diag2:
                continue
            usedRows.add(row)
            diag1.add(row - col)
            diag2.add(row + col)

            #compare original position with this row
            if queens[col] == row:
                step = 0
            else:
                step = 1
            
            backtrack(col+1, curSteps+step)

            usedRows.remove(row)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0, 0)
    return curMin