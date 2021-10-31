# Bubble sort冒泡排序

from typing import Mapping
import math


def bubble_sort(alist):
    # 相邻连个元素进行比较，如果发现位置错误则进行交换位置
    print(id(alist))
    length = len(alist)
    for k in range(length):
        for i in range(length-1-k):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        print(alist)
    print(alist)


# 如果传入的列表就是有序，只需要检测一轮，如果没有进行交换，则直接退出循环
def bubble_sort2(alist):
    # 相邻连个元素进行比较，如果发现位置错误则进行交换位置
    print(id(alist))
    length = len(alist)
    for k in range(length-1):
        count = 0
        for i in range(length-1-k):
            if alist[i] > alist[i+1]:
                count += 1
                alist[i], alist[i+1] = alist[i+1], alist[i]
        print(alist)
        if count == 0:
            break
    print(alist)


# 选择排序
# #
def selection_sort(alist):
    length = len(alist)
    for j in range(length-1):
        for i in range(length-j):
            if alist[j] > alist[i+j]:
                alist[j], alist[i+j] = alist[i+j], alist[j]
        print(i, j, " => ", alist)
    print(alist)


# 选择排序2 将最大的元素放到列表最后#
def selection_sort(alist):
    pass


# 插入排序 #
def insert_sort(alist):
    length = len(alist)
    for i in range(length):
        for j in range(i+1):
            if alist[i] < alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
                print("i => ", i, "j => ", j, alist)


def insert_sort2(alist):
    length = len(alist)
    for i in range(1, length):
        j = i
        while j > 0:
            # 此处循环将每个元素和有序列表中的每个元素进行比较 #
            if alist[j] < alist[j-1]:
                # 如果当前元素比前一个元素小，则进行交换 #
                alist[j], alist[j-1] = alist[j-1], alist[j]
            else:
                # 否则已经是有序列表，不需要交换了，退出当前循环 #
                break
            j -= 1
            print("i => ", i, "j => ", j, alist)



def quicksort(alist, start, end):
    """
    快速排序
    """
    # 递归退出条件
    print("start => ", start, "end => ", end)
    if start >= end:
        return
    # 基准数
    mid = alist[start]
    low = start
    high = end 

    while low < high:
            # 从左向右alist[high] > mid 则high -= 1
        while alist[high] > mid and low < high:
            high -= 1
            # 将high索引对应的元素赋值给low
        alist[low] = alist[high]
        # 从左到右 alist[low] < mid, 则low += 1
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    # 将基准数放置到对应的位置
    alist[low] = mid
    print(alist)

    # 比基准数小的即左边的数据，要重复调用quicksort
    quicksort(alist, start, low-1)
    # 比基准数大的即右边的数据，也要重复调用quicksort
    quicksort(alist, low+1, end)

# 归并排序 #
def merge_sort(alist):
    # 第一步 分解
    num = len(alist)
    # 递归结束条件 #
    if num <= 1:
        return alist
    mid = num // 2
    left_list = merge_sort(alist[0:mid])
    right_list = merge_sort(alist[mid:])
    # 第二步 合并
    result = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    # 退出循环之后，将不为空的列表剩余元素添加到result中 #
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    # 将结果返回 #
    return result

if __name__ == "__main__":
    alist = [7 ,4, 6, 9, 1]
    alist2 = [1, 2, 3, 4, 5]
    alist3 = [1, 2, 4, 3, 5]
    # print(id(alist))
    # bubble_sort(alist)
    # print(alist)
    # bubble_sort2(alist)
    # bubble_sort2(alist2)
    # bubble_sort2(alist3)
    # selection_sort(alist)
    alist4 = [54, 226, 93, 17, 77, 31,44, 55, 20]
    # insert_sort2(alist4)
    # quicksort(alist4, 0, len(alist4)-1)
    # print(alist4)
    res = merge_sort(alist4)
    print(res)