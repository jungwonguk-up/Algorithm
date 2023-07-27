import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
num = int(input())

check_list = [[],[]] 
num1 = 3
num2 = 5

check_list[1].append(num1)
check_list[1].append(num2)

if num == 3 or num == 5:
    print(1)
    sys.exit()

for lv in range(2,10000):
    check_list.append([])
    for num_check in check_list[lv-1]:
        check_list[lv].append(num_check + num1)
        check_list[lv].append(num_check + num2)
    check_list[lv] = set(check_list[lv])
    check_list[lv-2] = None
    if num in check_list[lv]:
        print(lv)
        break
    if num < min(check_list[lv]):
        print(-1)
        break