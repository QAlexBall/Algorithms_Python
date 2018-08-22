class Solution(object):
    def binaryGap(self, N):
        last = -1
        ans = 0
        for i in range(0, 32):
            if (N >> i) & 1 > 0:
                if last >= 0:
                    ans = max(ans, i - last)
                last = i
        return ans


test = Solution()
print(test.binaryGap(10))
