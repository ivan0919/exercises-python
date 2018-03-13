#寻找第6个默尼森数

#经典程序设计问题：找第n个默尼森数。
#P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。
#例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
#提交方式直接将答案（M的值）写在txt文件中通过网络提交。


import math
def isPrime(a):
    b = 0
    for i in range(2,int(math.sqrt(a) + 1)):
        if a % i == 0:
           b += 1
    if b == 0:
        return 1
    else:
        return 0
for i in range(2,10000):
    M = 2 ** i - 1
    if isPrime(i) == 1 and isPrime(M) == 1:
        print(M)