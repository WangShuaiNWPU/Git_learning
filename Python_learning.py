#-*- coding:utf-8 -*-


# import kNN1
# from numpy import *

# dataSet,labels = kNN1.creatDataSet()

# testX = array([1.2,1.0])
# k = 3
# outputLabel = kNN1.kNNClassify(testX,dataSet,labels,3)
# print ("your Input is:",testX,"and classified to class:",outputLabel)

# testX = array([0.1,0.3])
# outputLabel = kNN1.kNNClassify(testX,dataSet,labels,3)
# print ("your Input is:",testX,"and classified to class:",outputLabel)




# from numpy import *
# import kNN1
# datingDataMat,datingLabels = kNN1.file2matrix('E:\datingTestSet2.txt')
# import matplotlib
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,0],datingDataMat[:,1],
# 15.0*array(datingLabels),15.0*array(datingLabels))
# plt.show()




# from numpy import *
# import kNN1
# datingDataMat,datingLabels = kNN1.file2matrix('E:\datingTestSet2.txt')
# import kNN1
# normMat,ranges,minVals = kNN1.autoNorm(datingDataMat)
# print(minVals)


# import kNN1
# kNN1.datingClassTest()

# from numpy import *
# import kNN1
# kNN1.classifyPerson()


#import kNN1
#testVector = kNN1.img2vector('E:\zero13.txt')        #难道是该版本的python不支持0_13.txt的文件名格式？013.txt也不行
#print(testVector[0,0:31])
# hei = input('height=')
# height = float(hei)
# wei = input('weight=')
# weight = float(wei)
# print('height=',height)
# print('weight=',weight)
# bmi =weight/height**2
# if bmi <18.5:
    # print('过轻')
# elif bmi<=25:
    # print('正常')
# elif bmi <=28:
    # print('过重')
# elif bmi <=32:
    # print('肥胖')
# else:
    # print('严重肥胖')
    # pass

    
    
    
# #使用list和tuple

# L = [
    # ['Apple', 'Google', 'Microsoft'],
    # ['Java', 'Python', 'Ruby', 'PHP'],
    # ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])


#调用函数
# n1 = 255
# n2 =1000
# print(n1,' hexadecimal=',str(hex(n1)))
# print(n2,' hexadecimal=',str(hex(n2)))

#定义函数
# from e:\abstest import my_abs
# print(my_abs(-5))

#cmd进入该文件路劲。输入Python，进入Python界面。输入：from Python_learning import ***(函数名)，即可调用该函数。

#递归函数
# def fact(n):
    # if n==1:
        # return 1
    # return n*fact(n-1)
    
#练习题——汉诺塔
#n个盘子从a借助b移动到c
# def move(n,a,b,c,num=[1]):
    # if n==1:
        # print('第%s次：%s->%s' % (num[0],a,c))
        # num[0] = num[0]+1
        # return
    # else:
        # move(n-1,a,c,b)
        # print('第%s次：%s->%s' % (num[0],a,c))
        # num[0] = num[0]+1
        # move(n-1,b,a,c)
        
        
# #运算符迭代
# a = ['+','-','*','/']
# for i in a:
    # print(i)



    
#列表生成式
# L = []
# for x in range(1,11):
    # L.append(x*x)
# print(L)

# L1 = [x*x for x in range(1,11)]
# print(L1)
    
# L2 = [x*x for x in range(1,11) if x %2 == 0]
# print(L2)

# L3 = [m+n for m in 'ABC' for n in 'XYZ']
# print(L3)

# import os
# L4 = [d for d in os.listdir('.')]
# print(L4)

# d = {'x':'A','y':'B','z':'C'}
# for k,v in d.items():
    # print(k,'=',v)
    
# L5 = [k+'='+v for k,v in d.items()]
# print(L5)

# L = ['Hello','World','IBM','Apple']
# L6 = [s.lower() for s in L]
# print(L6)

# L = ['Hello','World',18,'IBM','Apple']
# L7 = [s1.lower() for s1 in L if isinstance(s1,str)]
# for s2 in L:
    # if isinstance(s2,str):
        # pass
    # else:
        # # print(L.index(s2))
        # L7.insert(L.index(s2),s2)
# print(L7)

# L = [x*x for x in range(10)]
# print('L=',L)

# g = (x*x for x in range(10))
# print('g=',g)

# g1 = (x*x for x in range(10))
# for n in g1:
    # print(n)

# def fib(max):
    # n,a,b = 0,0,1
    # while n<max:
        # print(b)
        # a,b = b,a+b
        # n = n+1
    # return 'done'
    
# def fib(max):
    # n,a,b = 0,0,1
    # while n<max:
        # yield b
        # a,b = b,a+b
        # n = n+1
    # return 'done'
    
# def odd():
    # print('step1:')
    # yield(1)
    # print('step2')
    # yield(3)
    # print('step3')
    # yield(5)
    
# o = odd()
# next(o)

# for n in fib(6):
    # print(n)
    
# g = fib(6)
# while True:
    # try:
        # x = next(g)
        # print('g:',x)
    # except StopIteration as e:
        # print('Generator return value:',e.value)
        # break

# def triangles():
    # a,b = 1,1
    # L = []
    # L1 = []
    # L = [1]
    # yield L
    # L = [1,1]
    # yield L
    # while True:
        # L = [L[n]+L[n+1] for n in range(len(L)-1)] 
        # L.insert(0,1)
        # L.append(1)
        # yield L
       
# n=0
# for t in triangles():
    # print(t)
    # n = n+1
    # if n == 10:
        # break

# f = abs
        
# def add(x,y,f):
    # return f(x)+f(y)
    
# out = add(-5,6,f)
# print(out)

#map和reduce的使用
# def f(x):
    # return x*x
   
# r = map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))

# L =[]
# for n in [1,2,3,4,5,6,7,8,9]:
    # L.append(f(n))
    
# print("L=",L)

# ###############
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# ###############
# from functools import reduce

# def add(x,y):
    # return x + y

# ws1 = reduce(add,[1,3,5,7,9])
# print("ws1=",ws1)

# ws2 = sum([1,3,5,7,9])
# print("ws2=",ws2)

# ##################
# from functools import reduce
# def fn(x,y):
    # return x*10 + y
    
# ws3 = reduce(fn,[1,3,5,7,9])
# print("ws3=",ws3)

# ####################
# from functools import reduce
# def fn(x,y):
    # return x*10 + y
    
# def char2num(s):
    # return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

# ws4 = reduce(fn,map(char2num,'13579'))
# print("ws4=",ws4)

# from functools import reduce

# def str2int(s):
    # def fn(x,y):
        # return x*10 + y
    # def char2num(s):
        # return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    # return reduce(fn,map(char2num,s))
    
# ws5 = str2int('13579')
# print("ws5=",ws5)

# #######练习题1##########
# def normalize(name):
    # num = len(name)
    # name_new = []
    # for i in range(num):
        # if i == 0:
            # if name[i].islower():
                # name_new.append(name[i].upper())
            # else:
                # name_new.append(name[i])
        # else:
            # if name[i].islower():
                # name_new.append(name[i])
            # else:
                # name_new.append(name[i].lower())
    # return ''.join(name_new)

# L1 = ['adam','LISA','barT']
# L2 = list(map(normalize,L1))
# print(L2)

# ##########练习题2########
# from functools import reduce
# def multi(x,y):
    # ws = []
    # for i in range(y):
        # ws.append(x)
    # return sum(ws)

# # print(multi(5,3))    
# def prod(L):
    # return reduce(multi,L)
    
# print("3*5*7*9=",prod([3,5,7,9]))

# ###########练习题3##########
# from functools import reduce
# def char2num(s):
    # return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

# def fn1(x,y):
    # return x*10+y
    
# def fn2(x,y):
    # return x*0.1+y
    
# def str2float(s):
    # s_1 = s[0:s.index('.')]
    # s_2 = s[(s.index('.')+1):]
    # s_2 = s_2[::-1]
    # float_1 = reduce(fn1,map(char2num,s_1)) 
    # float_2 = 0.1*reduce(fn2,map(char2num,s_2))
    # return float_1 + float_2
                    
# print('str2float(\'1234.4756\')=',str2float('1234.4756'))


#####filter
# def is_odd(n):
    # return n%2 ==1 
    
# print(list(filter(is_odd,[1,2,4,5,6,9,10])))

# def not_empty(s):
    # return s and s.strip()
    
# print(filter(not_empty,['A','','B',None,'C',' ']))

# def _odd_iter():
    # n = 1
    # while True:
        # n = n+2
        # yield n

# def _not_divisible(n):
    # return lambda x:x%n>0

# def primes():
    # yield 2
    # it = _odd_iter()
    # while True:
        # n = next(it)
        # yield n 
        # it = filter(_not_divisible(n),it)
        
########练习题 判断回数##
# def is_palindrome(n):
    # str_num = str(n)
    # length = len(str_num)
    # if length>=3:
        # if length%2 == 0:
            # n = int(length/2)
            # str_pre = list(str_num[0:n])
            # str_pos = list(str_num[n:length]).reverse()
            # return str_pre == str_pos
        # if length%2 == 1:
            # m = int((length-1)/2)
            # s = int((length+1)/2)
            # str_pre = list(str_num[0:m])
            # str_pos = list(str_num[s:length]).reverse()
            # return str_pre == str_pos
  
        
# output = filter(is_palindrome,range(1,1000))
# print(list(output))


# print('Hello World')


#########sorted#############
# print(sorted([36,5,-12,9,-21]))

# print(sorted([36,5,-12,9,-21],key = abs))

# print(sorted(['bob','about','Zoo','Credit']))

# print(sorted(['bob','about','Zoo','Credit'],key = str.lower))

# print(sorted(['bob','about','Zoo','Credit'],key = str.lower,reverse = True))


###练习题
# L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

# def by_name(t):
    # return t[0]
    
# L2 = sorted(L,key = by_name)
# print('按名字排名：',L2)

# def by_score(t):
    # return t[1]
    
# L3 = sorted(L,key = by_score,reverse = True)
# print('按成绩排名：',L3)


#########返回函数
# def calc_sum(*args):          #可变参数
    # ax = 0
    # for n in args:
        # ax = ax+n
    # return ax

# def lazy_sum(*args):
    # def sum():
        # ax = 0
        # for n in args:
            # ax = ax+n
        # return ax
    # return sum
    
# f = lazy_sum(1,3,5,7,9)
# print(f)

# def count():
    # fs = []
    # for i in range(1,4):
        # def f():
            # return i*i
        # fs.append(f)
    # return fs
    
# f1,f2,f3 = count()
# print(f1())
# print(f2())
# print(f3())

######匿名函数#########
# print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))

# f = lambda x:x*x
# print(f(5))

##########装饰器
# import functools

# def log(func):
    # def wrapper(*args,**kw):
        # print('call %s():' %func.__name__)
        # return func(*args,**kw)
    # return wrapper
    
# @log
# def now():
    # print('2016-6-25')
    
# now()

# print(now.__name__)

# def log(text):
    # def decorator(func):
        # def wrapper(*args,**kw):
            # print('%s %s();' % (text,func.__name__))
            # return func(*args,**kw)
        # return wrapper
    # return decorator 
     
# @log('execute')
# def now():
    # print('2015-06-25')
    
# now()

# print(now.__name__)

# import functools

# def log(func):
    # @functools.wraps(func)
    # def wrapper(*args,**kw):
        # print('call %():' % func.__name__)
        # return func(*args,**kw)
    # return wrapper
    
# import functools

# def log(text):
    # def decorator(func):
        # @functools.wraps(func)
        # def wrapper(*args,**kw):
            # print('%s %s():'%(text,func.__name__))
            # return func(*args,**kw)
        # return wrapper
    # return decorator
    
#练习题1

# import functools    
# def log(func):
    # @functools.wraps(func)
    # def wrapper(*args,**kw):
        # print('begin call')
        # func()
        # print('end call')
    # return wrapper
    
# @log
# def now():
    # print('2016-06-25')
    
# now()

#####练习题2########
# import functools
# def log(text=''):
    # def decorator(func):
        # @functools.wraps(func)
        # def wrappers(*args,**kw):
            # print('%s %s():' % (text,func.__name__))
            # return func(*args,**kw)
        # return wrappers
    # return decorator

# @log()
# def now():
    # print('2016-06-25')
    
# now()

# print(now.__name__)

##偏函数########
# def int2(x,base = 2):
    # return int(x,base)
    
import functools

# int2 = functools.partial(int,base = 2)

int2 = functools.partial(int,base = 2)

print(int2('1010101'))

print(int2('1010101',base = 10))






































