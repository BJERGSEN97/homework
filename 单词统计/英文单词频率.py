"""
@Author         :BJERGSEN97
@contact        :1345600853@qq.com
@Time           :2021/4/11 23:15
@File           :英文单词频率.py
@Description    :
@Learn          :
"""
"""
@Author         :BJERGSEN97
@contact        :1345600853@qq.com
@Time           :2021/4/11 17:12
@File           :9合并过去式、过去分词.py
@Description    :字典 值是原型
@Learn          :
"""
import re
def is_letter(s):
    if (s[0]=='1'or s[0]=='2' or s[0]=='3' or s[0]=='4' or s[0]=='5'or s[0]=='6'or s[0]=='7' or s[0]=='8' or s[0]=='9' or s[0]=='0'):
        return False
    return True

def testWord(data):
    data = data.lower()
    data = data.replace('.', ',')
    data = data.split(',')
    result = []
    #data1 = []
    for i in data:
        list_word = re.findall(r"[\w']+", i)
        data1 = []
        for j in list_word:
            if(is_letter(j)):
                data1.append(j)
        str_juzi = ' '.join(data1)
        result.append(str_juzi)
    while '' in result:
        result.remove('')
    return result

def ltrFreq(data):
    dict1 = {}
    dict2 = {}
    dict3 = {}
    data = ''.join(data)
    data = ''.join(data.split())
    #print(data)
    for i in range(len(data)):
        if (data[i] not in dict1):
            dict1[data[i]] = 1
        else:
            dict1[data[i]] = dict1[data[i]] + 1
    # print(dict1)
    #print(dict1)
    a = sorted(dict1.keys())
    for i in range(len(a)):
        dict2[a[i]] = dict1[a[i]]
    # print(dict2)

    b = sorted(dict2.values())
    for i in reversed(b):
        for j in dict2:
            if (dict2[j] == i):
                del dict2[j]
                dict3[j] = i
                break
    # print(dict3)

    for i in dict3.keys():
        dict3[i] = "%.2f%%" % (dict3[i] / len(data) * 100)
    return dict3


'''分词处理'''
def wordSegDict(data):
    dict1 = {}
    data = data.split('\n')
    #print(data)
    data2 = []
    for i in data:
        data1 = i.split(' ')
        data2.append(data1)
    while [''] in data2:           #!
        data2.remove([''])
    #print(data2)
    for i in data2:
        for j in i:
            if j not in dict1:
                dict1[j] = i[0]
    return dict1

def repWord(data,dict1):
    data2 = []
    for i in data:
        data1 = i.split(' ')
        for j in data1:
            if (j in dict1):
                #print(j)
                i = i.replace(j,dict1[j])
        data2.append(i)
    return data2

def letter(data):  #输入数据，生成各字母的百分数频率
    a = ' '
    data = a.join(data)
    dict1={}#统计
    dict2={}#排序
    dict3={}
    data = re.findall(r"[\w']+", data)
    #print(data)
    for i in data:
        if(not is_letter(i)):
            continue
        if (i not in dict1 ):
            dict1[i] = 1
        else:
            dict1[i] = dict1[i]+1
    a = sorted(dict1.keys())
    for i in range(len(a)):
        dict2[a[i]] = dict1[a[i]]
    b = sorted(dict2.values())
    for i in reversed(b):
        for j in dict2:
            if (dict2[j] == i):
                del dict2[j]
                dict3[j] = i
                break
    for i in dict3.keys():
        dict3[i] = "%.2f%%" % (dict3[i] / len(data) * 100)
    return dict3

def slide(data,n):
    result = []
    c = []
    for i in data:
        a = i.split(' ')
        for j in range(len(a)-n+1):
            result.append(a[j:j+n])
    return result

def freq(dict1,n):
    dict2 = {}#频率结果
    a = []
    for i in dict1.keys():
        a.append(i)
    b = a[:n]
    for i in b:
        dict2[i]=dict1[i]
    return dict2

def identifyN(n,len1):
    if(len(n) == 0):
        return int(len1)
    elif(int(n)<=len1):
        return int(n)
    else:
        return int(len1)

def stopWord(dict1,stopword,judgment):
    if(judgment == 'no'):
        a = dict1.keys()
        b = len(a)
        return dict1,b
    elif(judgment == 'yes'):
        sw = stopword.lower()
        sw = re.findall(r"[\w']+", sw)
        for i in sw:
            if(i in dict1):
                del dict1[i]
        a = dict1.keys()
        b = len(a)
        return dict1,b
    else:
        a = dict1.keys()
        b = len(a)
        print('输入有误默认不加入stopword')
        return dict1,b

def trgtWord(dic1,trgtword):
    dic2 = {}
    if (trgtword in dic1):
        dic2[trgtword] = dic1[trgtword]
        return dic2
    else:
        return {}

def generatePhrase(data):#生成词组
    result1 = []
    for i in data:
        str1 = str()
        for j in i:
            if(str1 == str()):
                str1 = str(j)
            else:
                str1 = str1+' '+str(j)
        result1.append(str1)

    return result1

def srtPhrases(data):#相同分成一类 并计算概率。
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for i in range(len(data)):
        if (data[i] not in dict1 ):
            dict1[data[i]] = 1
        else:
            dict1[data[i]] = dict1[data[i]]+1
    a = sorted(dict1.keys())
    for i in range(len(a)):
        dict2[a[i]] = dict1[a[i]]
    b = sorted(dict2.values())
    for i in reversed(b):
        for j in dict2:
            if (dict2[j] == i):
                del dict2[j]
                dict3[j] = i
                break
    for i in dict3.keys():
        dict3[i] = "%.2f%%" % (dict3[i] / len(data) * 100)
    return dict3

if __name__ == '__main__':
    f1 = open("article.txt", "r")  # 设置文件对象
    article = f1.read()  # 将txt文件的所有内容读入到字符串str中
    f1.close()
    #article = 'I take my book.I took my bag.I learned english.I am learning english.'
    f2 = open("pastForm.txt", "r")  # 设置文件对象
    pastForm = f2.read()  # 将txt文件的所有内容读入到字符串str中
    f2.close()

    f3 = open("stopword.txt", "r")  # 设置文件对象
    stopword = f3.read()  # 将txt文件的所有内容读入到字符串str中
    f3.close()  # 将文件关闭
    # stopword = 'i love'
    #print(pastForm)
    #pastForm =

    word = testWord(article)
    print(word)

    letter1 = ltrFreq(word)
    print(letter1)

    '''处理分词'''
    usedword = wordSegDict(pastForm)
    #print(usedword)

    replace = repWord(word,usedword)
    print(replace)

    numword = letter(replace)
    print(numword)

    judgment = input("请输入是否加入stop word(yes/no):")
    result1, len1 = stopWord(numword, stopword, judgment)
    print(result1)

    trgtword = input("请输入想要查找的单词:")
    propor = trgtWord(result1, trgtword)
    if (propor == {}):
        print("没有找到你想找到的单词")
    else:
        print(propor)

    n = input("请输入n值(要求n值小于%d,若不满足则输出所有单词频率）=" % len1)
    n1 = identifyN(n, len1)
    result2 = freq(result1, n1)
    print(result2)


    n = int(input("请输入需要的词组数量："))
    howManyPhrases = slide(replace, n)
    newphrases = generatePhrase(howManyPhrases)
    print(srtPhrases(newphrases))

