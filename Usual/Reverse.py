class Solution:
    def reverse(self, x):
        """
		:type x: int
		:rtype: int
		"""
        x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
        return x if 2147483648 > x >= -2147483648 else 0


print(Solution().reverse(123456))
x = 123456
print(str(x)[::-1])
