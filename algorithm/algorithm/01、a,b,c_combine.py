# 如果a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数)，如何求出a,b,c可能组合？
import time

def solution():
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a+b+c ==1000 and a**2 + b**2 == c**2:
                    print("a: %d, b: %d, c: %d" % (a, b, c))


def solution2():
    for a in range(1001):
        for b in range(1001):
            c = 1000 -a -b
            if a**2 + b**2 == c**2:
                print("a: %d, b: %d, c: %d" % (a, b, c))



# T(n) = k *f(n) +c 
# f(n) = n * n 
# f(n)叫做T(n)的渐进函数 
# solution的时间复杂度就是O(n^3) 
# solutiosn2的时间复杂度就是O(n^2) #




if __name__ == "__main__":
    start_time = time.time()
    # solution()    # 109s
    solution2()     # 1.6s
    end_time = time.time()
    print("花费时间： ", end_time-start_time)

