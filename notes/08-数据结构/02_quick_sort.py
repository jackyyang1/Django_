# [3,6,1,5,2]


def quick_sort(li, start, end):
    # 定义两个游标
    left = start
    right = end

    # 递归停止条件
    if start >= end:
        return

    # 定义中间值，把左边游标的数据作为中间值
    mid = li[left]

    while left < right:

        # 从右边开始，右边游标往左移动，找到小于mid的值，放到左边游标位置
        while left < right and li[right] >= mid:
            right -= 1
        # while循环结束时，right指向的数据是小于mid，放到左边游标位置
        li[left] = li[right]

        # 从左边开始，左边游标往右移动，找到大于等于mid的值，放到右边游标位置
        while left < right and li[left] < mid:
            left += 1
        # while循环结束时，left指向的数据是大于等于mid，放到右边游标位置
        li[right] = li[left]

    # while循环结束后 left=right，把mid值放到此位置
    li[left] = mid

    # 递归处理左边数据
    quick_sort(li, start, left-1)
    # 递归处理右边数据
    quick_sort(li, left+1, end)

if __name__ == '__main__':
    l = [5,4,3,1,1]

    # 3 [2,1,1,5,6]
    quick_sort(l,0,len(l)-1)
    print(l)

    # 最坏时间复杂度 O(n^2)
    # 最优时间复杂度 O(nlogn)
    # 稳定性 不稳定
