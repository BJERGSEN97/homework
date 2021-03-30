"""
@Author         :BJERGSEN97
@contact        :1345600853@qq.com
@Time           :2021/3/11 21:50
@File           :口算test.py
@Description    :口算器：题目显示在math.txt中
"""


from random import randint
n = int(input("请输入n值="))

fobj = open('math.txt', 'w')  #读取需要写入文档


def ZhengChu(nums):    #随机返回被除数的一个约数
    result = [a for a in range(1, nums + 1) if nums % a == 0]
    b = randint(0,len(result)-1)
    return result[b]


'''
一个类似于栈的结构，对于加减法，直接放到堆栈里（减法取相反数），乘除法进行运算后再放入堆栈，最后将堆栈的数直接相加
'''
def calculate(s) :

    n = len(s)
    stack = []
    preSign = '+'
    num = 0
    beichushu = 0
    re = []
    for i in range(n):
        if s[i] != ' ' and s[i].isdigit():
            num = num * 10 + ord(s[i]) - ord('0')  # 考虑有两位数的存在
        if i == n - 1 or s[i] in '+-*/':
            if preSign == '+':
                stack.append(num)
            elif preSign == '-':
                stack.append(-num)
            elif preSign == '*':
                stack.append(stack.pop() * num)
            else:
                abc = int(stack.pop())
                if(abc>0):
                    beichushu = ZhengChu(abc)
                    stack.append(int((abc / beichushu)))
                    re.append(beichushu)
                elif(abc==0):
                    stack.append(int(0))
                else:
                    abc=-abc
                    beichushu = ZhengChu(abc)
                    stack.append(-int(abc / beichushu))
                    re.append(beichushu)
                # print(abc)
                # beichushu = ZhengChu(abc)
                # print(beichushu)
                # stack.append(-int(abc / beichushu))
            preSign = s[i]
            num = 0
    return sum(stack),re

op=['+','-','*','/'] #随机生成加减乘除
for i  in range(n):
    TwoOrThree=randint(2,3)
    if(TwoOrThree == 2):
        a = randint(0, 100)
        b = randint(0, 100)
        c = randint(0, 100)
        d1 = randint(0, 3)#第一个运算符
        d2 = randint(0, 3)#第二个运算符

        first = op[d1]
        second = op[d2]
        result = 0
        chushulist = []
        str1 = str(str(a)+first+str(b)+second+str(c))
        result,chushulist = calculate(str1)

        #以下主要讨论被除数安放的位置
        if (len(chushulist)==0):
            fobj.writelines(str(a)+first+str(b)+second+str(c)+'='+str(result) + '\r' )
        elif(len(chushulist)==1 and d1 ==3):
            fobj.writelines(str(a) + first + str(chushulist[0]) + second + str(c) + '=' + str(result) + '\r' )
        elif(len(chushulist)==1 and d2 ==3):
            fobj.writelines(str(a) + first + str(b) + second + str(chushulist[0]) + '=' + str(result) + '\r' )
        else:
            fobj.writelines(str(a) + first + str(chushulist[0]) + second + str(chushulist[1]) + '=' + str(result) + '\r' )


    if(TwoOrThree == 3):
        a = randint(0, 100)
        b = randint(0, 100)
        c = randint(0, 100)
        d = randint(0, 100)
        d1 = randint(0, 3)  # 第一个运算符
        d2 = randint(0, 3)  # 第二个运算符
        d3 = randint(0, 3)  # 第3个运算符
        first = op[d1]
        second = op[d2]
        third = op[d3]
        result = 0
        chushulist = []
        str2 = str(str(a)+first+str(b)+second+str(c)+third+str(d))
        result, chushulist = calculate(str2)
        # 以下主要讨论被除数安放的位置
        if (len(chushulist) == 0):
            fobj.writelines(str2 +'='+str(result)+ '\r')
        elif (len(chushulist) == 1 and d1 == 3):
            fobj.writelines(str(a) + first + str(chushulist[0]) + second + str(c) +third+str(d)+ '=' + str(result) + '\r' )
        elif (len(chushulist) == 1 and d2 == 3):
            fobj.writelines(str(a) + first + str(b) + second + str(chushulist[0]) +third+str(d)+ '=' + str(result)+ '\r' )
        elif (len(chushulist) == 1 and d3 == 3):
            fobj.writelines(str(a) + first + str(b) + second + str(c) + third + str(chushulist[0]) + '=' + str(result)+ '\r' )
        elif(len(chushulist) == 2 and d1 == 3 and d2 ==3):
            fobj.writelines(str(a) + first + str(chushulist[0]) + second + str(chushulist[1]) + third + str(d) + '=' + str(result)+ '\r' )
        elif (len(chushulist) == 2 and d2 == 3 and d3 == 3):
            fobj.writelines(str(a) + first + str(b) + second + str(chushulist[0]) + third + str(chushulist[1]) + '=' + str(result)+ '\r' )
        elif (len(chushulist) == 2 and d1 == 3 and d3 == 3):
            fobj.writelines(str(a) + first + str(chushulist[0]) + second + str(c) + third + str(chushulist[1]) + '=' + str(result)+ '\r' )
        else:
            fobj.writelines(str(a) + first + str(chushulist[0]) + second + str(chushulist[1]) + third + str(chushulist[2]) + '=' + str(result)+ '\r' )