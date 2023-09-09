#Find the Difference
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        S=list(s)
        T=list(t)
        result =[]
        if len(S) > len(T):
            for i in S :
                if i in T :
                    T.remove(i)
                else:
                    result.append(i)
        elif len(T) > len(S):
            for i in T :
                if i in S :
                    S.remove(i)
                else:
                    result.append(i)
        return ''.join(result)
