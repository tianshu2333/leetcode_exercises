class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(int(len(nums))):
            for j in range(i+1,int(len(nums))):
                if nums[i]+nums[j] == target:
                    return(i,j)

#暴力解法，按照顺序查找，时间复杂度为O(n^2)
#时间复杂度：O(N^2)O(N 2 )，其中 NN 是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。空间复杂度：O(1)O(1)。
#Solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable: #判断对于一个num，其互补的数（target-num）是否在其右侧。如果在右侧有出现的话，则if为true返回实际数字。
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i #如果没有，则将左侧的数字存入哈希表，用于后续比对
        return []
#利用哈希表，每一次比较target-num和num的关系
#通过if 可以判定是否存在于哈希表，从而避免了再使用一次for查找target-num
