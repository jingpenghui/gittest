#!/usr/bin/python
#-*-coding:utf8-*-
# a = (1,2,3,4,5,6,7,8,9)
#
# print(a[2::3])#每3个一组打印每组下标2的数据
#a.count()统计
#a.index()


#dict#(字典) 格式：键值对组成
#变量名={key1 ：value1，
#        key2 ：value2}
#特点：1.无序的  2.见=键必须唯一  3.不支持索引和切片  4.可变的
# a = {'name' : 'zhang',
#           'age' : 12,
#           'n' : 'qwe'}
# #a.popitem() #默认删除最后一个
# a.pop('name')  # 根据键删除数据
# a.keys()  #获取所有的key
# print(a.values())  #获取所有的值
# print(a.items())  #获取所有的键值对
# update
#print(a)
# a = {'k1':'asd','k2':'abc','k3':'Abc','k4':'adf'}
# for i in a.values():
#     if i.startswith('a') or i.startswith('A'):
#         if i.endswith('c'):
#             print(i)

# a = [11,22,33,44,55,66,77,88,99]
# b ={'k1':[],'k2':[]}
# for i in a:
#     if i > 66:
#         b['k1'].append(i)
#     else:
#         b['k2'].append(i)
# print(b)
#set(集合） 格式：变量名={数据1，数据2}
#特点：1.=无序的，不重复 2.不支持索引和切片  3.可变的
#a = {1,74242,54324,3.433433,52329,1,1,2,3,5,8,4,6}
#  添加数据a.add(0)
# 删除数据
# 删除指定数据a.remove(1)
# 随机删除一个a.pop()
# | 并集   & 交集    - 差集
#print(a)
# a = ['weqe','asd','zcx','fdgh']
# b = {'name':123,'avg':12}
# for i,j in b.items():     #enumerate(a):
#      print(i,j)

#列表推导式：
#讲条件控制语句写在列表中，产生的结果会自动存储在列表中
#格式;[语句的结果  条件控制语句]
#计算10以内每个偶数的平方，放在列表中

# a = [i**2 for i in range(2,11,2)]
# print(a)
# a = [11,22,33,44,55,66,77,88,99]
# b = [ i for i in a if i > 55]
# print(b)

# def oushu():
#     a = 0
#     for i in range(2,101,2):
#         a+=i
#     print(a)
# def jishu():
#     b = 0
#     for j in range(1,100,2):
#         b+=j
#     print(b)
#globals 变量名  # 将局部变量变成全局变量
#def 函数（参数） 必须参数 ：必须填写的参数
#def 函数名（参数名=值)：
#def 函数名（*args）：   一次性可以传入很多数据，接受到的数据类型是元组
#def 函数名 （**kwargs）： 传入的数据必须是键值对格式，数据类型是字典
#优先级： 必须参数》默认参数》可变长参数


#return 返回值    作用：将return后面的数据赋值给函数  2.结束函数
#格式：def 函数名（）：
          # 执行语句块
          # return 数据
# txt=open(r'c:\Users\jingpenghui\Desktop\b.txt','w',encoding='utf8')
# txt.write('nihao\n'*10)
# txt.write('')

# for i in range(10):
#     for j in range(1,i+1):
#         txt.write('%d*%d=%d\t' %(i,j,i*j))
#     txt.write('\n')
#
# for a in range(101):
#     for b in range(1,5):
#         txt.write('123\t')
#     txt.write('\n')
# def aaa(a,b,c):
#     print(a,b,c)
#     def qqq(q,w):
#         print(q,w)
#     return qqq
# aaa(1,2,1)(12,23)
# def qqq(a,name='asd',kk='123'):
#     print(a,name,kk)
# qqq([12,34,45],12,1234)
#
# a=open(r'C:\Users\jingpenghui\Desktop\80cb39dbb6fd5266ee9799fca518972bd507369d-1.jpg','rb')
# b=a.read()
# print(b)
# a.close()
# c=open('a.jpg','wb')
# c.write(b)
# print(c)
# c.close()

# with open('a.txt','r') as f:
#     print(f.read())
