# 如果a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数)，如何求出a,b,c可能组合？
import time

def solution():
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a+b+c ==1000 and a**2 +b**2 == c**2:
                    print("a: %d, b: %d, c: %d" % (a, b, c)) 


if __name__ == "__main__":
    start_time = time.time()
    solution()
    end_time = time.time()
    print("花费时间： ", end_time-start_time)

