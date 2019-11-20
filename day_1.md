### 题目描述

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

### 解题思路
- 自己
已知数组是排序好的，判断数组中某个元素是否重复
相当于比较该元素与其前一个元素是否相等
如果相等，去掉该元素


### 代码
- 自己——单指针
```Python
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
```

- 参考——双指针
```Python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0; j = 1 
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1               
        return i + 1


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    solu = Solution()
    count = solu.removeDuplicates(nums)
    for i in range(count):
        print(nums[i])
```
### 复杂度分析
- 空间复杂度：O(1)
- 时间复杂度：O(n);
数组元素个数为n，数组nums的未重复元素有count个，单指针的循环次数就是count；
双指针的循环次数是n-1次

### LeetCode得分
- 单指针
<img src='grade_day_1.png'>
- 双指针
<img src='grade_day_1_double.png'>

