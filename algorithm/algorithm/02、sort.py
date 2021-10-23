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
    insert_sort2(alist4)
