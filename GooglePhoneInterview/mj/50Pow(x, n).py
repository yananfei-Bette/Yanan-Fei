# 50 Pow(x, n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # first we use brute force
        # time: O(n)
        '''
        def multiply(x, n):
            res = 1
            for i in xrange(1, n + 1):
                res *= x
            return res
            
        mark = 0
        if n < 0:
            mark = 1
            n = -n
        return multiply(x, n) if mark == 0 else 1.0/multiply(x, n)
        '''
        
        # recursive method
        # time: O(logn)
        # space: O(logn)
        '''
        def helper(x, n):
            if n == 0:
                return 1
            res = helper(x, n/2)
            if n%2 == 0:
                return res*res
            return res*res*x
        
        mark = 0
        if n < 0:
            mark = 1
            n = -n
        return helper(x, n) if mark == 0 else 1.0/helper(x, n)
        '''
        
        # interative method
        # time: O(logn)
        # space: O(1)
        mark = 0
        if n < 0:
            mark = 1
            n = -n
        
        res = 1
        curr = x
        i = n
        while i > 0:
            if i%2 == 1:
                res *= curr
            curr *= curr
            i /= 2
            
        return res if mark == 0 else 1.0/res
        