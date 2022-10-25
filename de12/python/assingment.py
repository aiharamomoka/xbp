import random

name=input("名前を教えてください")

def user_num():
    num = int(input('数字を入力してください：\n'))
    return num
def max_num():
    max_num = int(input('最大数値を入力：\n'))
    return max_num
def min_num():
    min_num = int(input('最小数値を入力：\n'))
    return min_num
        
min_num,max_num = min_num(),max_num()
 
while True:
    res = random.randint(min_num,max_num)
    if res!=min_num and res!=max_num:
        break
f = [min_num,max_num]

def comp(a,b):
    if a>b:
        f[1] = a
    else:
        f[0] = a
    print("範囲はから{}まで{}，もう一回入力してください".format(f[0],f[1]))
 
flag = 0
while True:
    num = user_num()
    if num not in range(f[0],f[1]):
        print("範囲外")
        continue
    elif num!=res:
        comp(num,res)
    elif num==res:
        print("BOOM！")
        break
    flag += 1
print("残念、%d回目で爆発した。"%flag)