class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        frequency_array = {}
        
        out = [1] if A[0] == B[0] else [0]
        
        for i in range(1, len(A)):
            print(A[i], B[:i+1])
            if A[i] in B[:i+1]:
                out.append(out[i-1]+1)
            else: 
                out.append(out[i-1])
        return out

test = [1, 3, 2, 4], [3, 1, 2, 4]
print(Solution().findThePrefixCommonArray(*test))
