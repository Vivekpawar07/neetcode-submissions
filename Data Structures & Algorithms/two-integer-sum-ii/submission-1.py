class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashs = {}
        for i,num in enumerate(numbers):
            diff = target - num
            if diff in hashs:
                return[hashs[diff] +1,i+1]

            hashs[num] = i
            