#print("hello bowen")
# # # print("你好 世界")
# # # print("你好 博文")
# # # print("你好 中国")
# # # print("你好 世")
# # # print(2+3)
# # # a = 3
# # # b = 4
# # # print(a+3)
# # # print(a+b)
# # # aa = 576547816
# # # bb = 111111
# # # print(aa)
# a = int(input("输入数："))
# if 100 >= a >= 0:
#     if a >= 60:
#         if a >= 70:
#             if a >= 90:
#                 print("优秀")
#             else:
#                 print("一般")
#         else:
#             print("及格")
#     else:
#         print("不及格")
# else:
#     print("请重新输入")
# a =  input("请输入一串字符：")
# b = list(set(a)) # 把a的类型定义成 集合（集合：无序的、不重复的）和 列表类型 成为 b
# c = []
# for d in b:# b现在是 不重复的一个列表，从b中取d
#     e = str(a.count(d))# 统计出来 a中有几个d （ e 是数字 ），注意 把a定义成字符串形式统计
#     c.append(d + e)#把数字与字母相加 ，成为新的字符串
#     c.sort(reverse=True)#排序
# print(c)
# for f in c:# f 是 c列表 里 的值
#     print(f[0],end=' ') #把列表的第一个数字的 最后一位取出来 例：400c   c 为最后一个



goods=[{'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},{'name':'美女','price':998}]
zz = int(input("您的总资产："))
for f,g  in enumerate(goods):
    print(f, goods[f]["name"], goods[f]["price"])
d = 0
gw=[]
while 1:
    a= int(input("请输入你要加入购物车的商品的编号："))
    b = [a,goods[a]["name"], goods[a]["price"]]
    gw.append(b)
    print(gw)
    c=goods[a]["price"]
    d += c
    yc = input('是否移除商品：（0是1否）')
    if yc == '0':
        q = int(input('输入要删除的序号：'))
        d -= gw[q][-1]
        gw.remove(gw[q])
    else:
        print('不删除')
    zf = input('是否付款：（0是1否）')
    if zf == '0':
        print('应付%d' %d)
        break
    else:
        print('继续购买')
while 1:
    if d > zz:
        print('余额不足,剩余%d' %zz)
    else:
        print('购买成功,剩余%d' %(zz-d))
        break
    cz = int(input('输入充值金额：'))
    zz+=cz


