# transfer to decimal
def todecimal(mylist):
    cur_base = mylist[0][0]
    base = mylist[0][1]
    num = mylist[1][0]
    if num < 10:
        new_list = [[cur_base, base], num * cur_base]
    else:
        new_list = [[cur_base, base], num / base]
        todecimal(new_list)

def tobase(base_list):
    cur_base = base_list[0][0]
    base = base_list[0][1]
    n = base_list[1][0]
    convString = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0
    if n < base:
        return convString[n]
    else:
        list = [[cur_base,base], (n / base**i) % base]
        return tobase(list)

input_list = eval(input())
input_list = todecimal(input_list)
print(tobase(input_list))



#Solution2

def c_m_10(num,m):
    num = int(str(num),base = m)
    return num

def c_10_m(num,n):
    res = ""
    while num:
        res = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = num // n
        print(res,num)
    return res

def m_10_n(num,m,n):
    return c_10_m(c_10_m(num,m),n)

m,n = map(int,input().split())
num = input()
print(m_10_n(num,m,n))