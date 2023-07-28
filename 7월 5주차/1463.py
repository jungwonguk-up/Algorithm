import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

num = int(input())

def three(num):
        return num//3

def two(num):
        return num//2

def one(num):
    return num-1

check_list = [[num]]

flag = True
cnt = 1

if num == 1:
    print(0)
    sys.exit()

while flag == True:
    tmp = []
    for i in check_list[cnt - 1]:
        tmp.append(one(i))
        if i % 2 == 0:
            tmp.append(two(i))
        if i % 3 == 0:
            tmp.append(three(i))
    tmp = set(tmp)
    check_list.append(tmp)
    if 1 in check_list[cnt]:
        print(cnt)
        flag = False
        break
    cnt += 1

