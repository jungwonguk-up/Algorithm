import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline()

def sol(num):
    check_list = [[0]]
    flag = True
    lv = 0
    cnt = 0
    while flag == True :
        if check_list[lv][0] >= num:
            print(cnt)
            break
        lv += 1
        tmp = []
        for i in check_list[lv -1]:
            tmp.append(i + 1)
            tmp.append(i + 2)
            tmp.append(i + 3)
        tmp.sort()
        for j in tmp:
            if j == num:
                cnt += 1
        check_list.append(tmp)


for i in range(int(input)):
    num = sys.stdin.readline()
    sol(int(num))
