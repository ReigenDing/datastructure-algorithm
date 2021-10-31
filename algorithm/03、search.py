# 查找算法 


# 顺序查找法#


def sequence_search(alist, value):
    for i in range(len(alist)):
        if alist[i] == value:
            return i
    return -1


# 二分查找法 #
# 二分查找法非递归实现 #
def binary_search(alist, value):
    n = len(alist)
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        print("mid => ", mid)

        # 判断中间值和比较值 #
        if alist[mid]  == value:
            return True
        elif alist[mid] > value:
            end = mid -1
        else:
            start = mid + 1
    return False

if __name__ == "__main__":
    test_case = [3, 5, 6, 9, 10, 78, 90]
    index =  sequence_search(test_case, 8)
    if index != -1:
        print("search successs!!")
    else:
        print("search faild")
    print(binary_search(alist=test_case, value=3))




