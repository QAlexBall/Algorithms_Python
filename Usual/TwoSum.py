class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if (target - num) in dic:
                return dic[target - num], i
            dic[num] = i


def main():
    nums = [2, 7, 11, 13]
    target = 9
    print(Solution().twoSum(nums, target))


if __name__ == '__main__':
    main()
