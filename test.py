class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        out = [1] if A[0] == B[0] else [0]
        for i in range(1, len(A)):
            out.append(out[i-1])
            if A[i] == B[i]:
                out[i] += 1
                continue
            if A[i] in B[:i+1]:
                out[i] += 1
            if B[i] in A[:i+1]:
                out[i] += 1
        return out

test = [1, 3, 2, 4], [3, 1, 2, 4]
print(Solution().findThePrefixCommonArray(*test))
