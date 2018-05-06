# [3,6,1,5,2]


def merge_sort(li):
    # 递归停止条件 只有一个数据时不继续拆分
    n = len(li)
    if n == 1:
        # print(li)
        return li
    # 从中间位置拆分数据
    mid = n//2

    left = li[:mid]
    right = li[mid:]
    # print(left)
    # print(right)

    # 递归拆分
    left_res = merge_sort(left)
    right_res = merge_sort(right)
    # res = left_res + right_res
    # print(res)
    # 把下层返回的数据 排序再返回给上层
    res = merge(left_res,right_res)
    return res


def merge(left, right):
    """把两个有序序列再组成有序序列"""
    # 3 6    1 2   5 6
    # 两个列表分别从0位置开始比较
    left_index = 0
    right_index = 0

    # 创建临时列表，保存结果
    res = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1
    # while循环结束时，只能处理完一个列表，需要把另一个列表剩下的数据加进来
    res = res + left[left_index:]
    res = res + right[right_index:]
    return res

if __name__ == '__main__':
    l = [5,4,3,2]
    print(merge_sort(l))

    # ll = [3,6,7,9]
    # rl = [1,2,5,8]
    # [1,2,3,5,6]
    # print(merge(ll,rl))

    # 最坏时间复杂度 O(nlogn)
    # 最优时间复杂度 O(nlogn)
    # 稳定性 稳定