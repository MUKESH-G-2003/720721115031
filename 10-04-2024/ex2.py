class Solution:
    def singleNumber(self, nums):
        answer = 0
        for num in nums:
            answer ^= num
        return answer

result = Solution()
nums = [2,2,1]

print(result.singleNumber(nums))