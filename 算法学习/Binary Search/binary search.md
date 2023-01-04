# 二分查找算法(Binary Search)

+++

二分查找算法（Binary Search）是一种在有序数组中查找某一特定元素的搜索算法。下面用 Python 实现二分查找的实例

arr = [1,2,3,4,5,6,7,8,9,10]
target = 7

1. 首先、定义"下限值low"和"上限值high = len(arr) - 1"

2. 寻找数组中的下标，即进入whilr循环(上限值大于或等于下限值)，寻求： 下标(mid) = (下限值(low) + 上限值(high)) // 2

3. 进入if-elif-else判断：

   1>. 当前下标小于目标值，则下限值(low) = 下标(mid) + 1

   2>. 当前下标大于目标值，则上限值(high) = 下标(mid) - 1

   3>. 当前下标等于目标值，则返回当前下标结果

4. 在while循环未找到目标值，则返回-1，目标未在数组中

5. 函数调用，设置数组，目标值，函数调用，返回判断，输出结果

```python
# 二分查找函数封装
def binary_search(arr, target):
  low = 0
  high = len(arr)-1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] < target:
      low = mid + 1
    elif arr[mid] > target:
      higt = mid - 1
    else:
      return mid
   return -1		# not found
```

函数调用

```python
arr = [1,2,3,4,5,6,7,8,9,10]
target = 7
index = binary_search(arr, search)
if index == -1:
  print(f"{target} not found in the index")
else:
  print(f"{target} found at index {index}")
```

这个函数会在数组“arr”中二分查找元素“target”，如果找到了，就返回它在数组中的下标，否则返回-1；
