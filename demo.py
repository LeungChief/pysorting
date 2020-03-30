'''
    计数排序
'''
def countingSort(nums):
    bucket = [0] * (max(nums) + 1)  # 桶的个数
    for num in nums:  # 将元素值作为键值存储在桶中，记录其出现的次数
        bucket[num] += 1
    i = 0  # nums 的索引
    for j in range(len(bucket)):
        while bucket[j] > 0:
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums


'''
    堆排序
'''
# 大根堆（从小打大排列）
def heapSort(nums):
    # 调整堆
    def adjustHeap(nums, i, size):
        # 非叶子结点的左右两个孩子
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        # 在当前结点、左孩子、右孩子中找到最大元素的索引
        largest = i
        if lchild < size and nums[lchild] > nums[largest]:
            largest = lchild
        if rchild < size and nums[rchild] > nums[largest]:
            largest = rchild
        # 如果最大元素的索引不是当前结点，把大的结点交换到上面，继续调整堆
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            # 第 2 个参数传入 largest 的索引是交换前大数字对应的索引
            # 交换后该索引对应的是小数字，应该把该小数字向下调整
            adjustHeap(nums, largest, size)
    # 建立堆
    def builtHeap(nums, size):
        for i in range(len(nums)//2)[::-1]: # 从倒数第一个非叶子结点开始建立大根堆
            adjustHeap(nums, i, size) # 对所有非叶子结点进行堆的调整
        # print(nums)  # 第一次建立好的大根堆
    # 堆排序
    size = len(nums)
    builtHeap(nums, size)
    for i in range(len(nums))[::-1]:
        # 每次根结点都是最大的数，最大数放到后面
        nums[0], nums[i] = nums[i], nums[0]
        # 交换完后还需要继续调整堆，只需调整根节点，此时数组的 size 不包括已经排序好的数
        adjustHeap(nums, 0, i)
    return nums  # 由于每次大的都会放到后面，因此最后的 nums 是从小到大排列



'''
    快速排序
'''
def quickSort(nums):  # 这种写法的平均空间复杂度为 O(nlogn)
    if len(nums) <= 1:
        return nums
    pivot = nums[0]  # 基准值
    left = [nums[i] for i in range(1, len(nums)) if nums[i] < pivot]
    right = [nums[i] for i in range(1, len(nums)) if nums[i] >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)

'''
@param nums: 待排序数组
@param left: 数组上界
@param right: 数组下界
'''
def quickSort2(nums, left, right):  # 这种写法的平均空间复杂度为 O(logn)
    # 分区操作
    def partition(nums, left, right):
        pivot = nums[left]  # 基准值
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]  # 比基准小的交换到前面
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]  # 比基准大交换到后面
        nums[left] = pivot # 基准值的正确位置，也可以为 nums[right] = pivot
        return left  # 返回基准值的索引，也可以为 return right
    # 递归操作
    if left < right:
        pivotIndex = partition(nums, left, right)
        quickSort2(nums, left, pivotIndex - 1)  # 左序列
        quickSort2(nums, pivotIndex + 1, right) # 右序列
    return nums


'''
    归并排序
'''

def mergeSort(nums):
    # 归并过程
    def merge(left, right):
        result = []  # 保存归并后的结果
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:] # 剩余的元素直接添加到末尾
        return result
    # 递归过程
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)
