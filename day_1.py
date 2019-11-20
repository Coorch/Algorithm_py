"""


给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array

"""

'''
思路
由于数组是已经排序好的，判断某个元素是否与之前的元素重复，只需判断是否与其前一个元素相等即可
'''
class Solution(object):
    def removeDuplicates(self, nums: [int]) -> int:
        count = 1 
        while count < len(nums):
            if nums[count] == nums[count-1]:
                nums.pop(count)
            else:
                count += 1                
        return count


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    solu = Solution()
    count = solu.removeDuplicates(nums)
    for i in range(count):
        print(nums[i])