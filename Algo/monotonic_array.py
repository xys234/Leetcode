"""



"""



class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 0
        decreasing, increasing = False, False
        while i <= len(A)-2:
            if A[i] < A[i+1]:
                increasing = True
            elif A[i] > A[i+1]:
                decreasing = True
            if increasing and decreasing:
                return False
            i += 1
        return True


if __name__ == '__main__':
    # case = [1,2,3,3]
    # case = [6,5,4,4]
    case = [11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]
    sol = Solution()
    print(sol.isMonotonic(case))
