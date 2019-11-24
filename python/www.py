# i = 0
# a = 0
# while i <= 100:
#     a += i
#     i = i+1
# print(a)
# i = 1
# a = 1
# while i <= 10:
#     a = i * a
#     i = i + 1
# print(a)
# i = 0
# a = 0
# while i <= 100:
#     if i % 2 != 0:
#         a += i
#     i = i+1
#     print(a)
# a = 1
# while a <= 9:
#     i = 1
#     while i <= a:
#         print("%d * %d = %d" %(i,a,a*i),end="\t")
#         i += 1
#     print("")
#     a += 1
# a = 2
# c = 0
# while a <= 100:
#     b = 2
#     while b < a:
#         if a % b ==0:
#             break
#         b += 1
#     else:
#         c = c + a
#     a += 1
# print(c)
# #
# a = 100
# while a <= 999:
#     b = a // 100
#     c = (a - b * 100) // 10
#     d = a - b*100 - c*10
#     if b**3 + c**3 + d**3 == a:
#         print(a)
#     a += 1
# a = [12,23,34]
# for i in a:
#     print(i)
# for i in range(2,100):
#     print(i)
# a = bool(input("是否有车票(o没有，1有):"))
# if a == 1:
#     print("")
#     b = int(input("请输入刀的长度："))
#     if b < 20:
#         print("请候车")
#     else:
#         print("刀长%d，不能上车" % b)
# else:
#     print("请购买车票")
# a = 0
# b = 0
# c = 0
# while b <= 99:
#     if b % 2 == 0:
#         a += b
#         b += 1
#     else:
#         c += b
#         b += 1
# print(c - a)
# c = input("请输入：")
# if "a" in c and "d" in c:
#     print(123)
# elif "a" in c:
#     print(456)
# elif "d" in c:
#     print(789)
# else:
#     print("没了")
# a = [11,22,33,33,33,44,55,66]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# a = [99,88,88,88,88,88,88,88,77,77,66,55]
# for i in a:
#     if a.count(i) > 1:
#         for j in range(a.count(i)-1):
#             a.remove(i)
# print(a)
#
# def sum1(x=1,y=100):
#     for i in range(x,y):
#         a = 0
#         for j in range(1,i):
#             if i%j==0:
#                 a +=j
#         if a == i:
#             print(a)
#
# sum1(100,1000)
#爬水井
# a = int(input('爬:'))
# b = int(input('掉：'))
# c = int(input('高：'))
# d=0
# i=1
# while 1:
#     d+=a
#     if d<c:
#         d-=b
#     elif d>=c:
#         break
#     i+=1
# print(i)

import time
# second=time.time()
# print(second)
# shijain=time.localtime()
# print(shijain)
# utc_shijain=time.gmtime()
# print(utc_shijain)
# geshihua=time.strftime('%y/%m/%d %H:%M:%S',time.localtime())
# print(geshihua)
# shijian=time.strftime('2019-10-29-43-2 09:49:47' '%y-%m-%d-%W-%w %X')
# print(shijian)

# jiegouhua=time.strptime('2019/10/28 18:00:00','%Y/%m/%d %X')
# shijian=time.mktime(jiegouhua)
# print(shijian)
# from time import *
# start=time()
# for i in range(3):
#     print(i)
#     sleep(3)
# end=time()
# print('时间%f'%(end-start))
# a=[1,2,3,4,5]
# b=['9','8','7','6','5']
# yaosuo=zip(a,b)
# for i,j in yaosuo:
#     print(i,j)

import requests   #  urllib2  urllib3   httpclient
import re         #  bs4   xpath
import pymysql

class Zhi_L(object):
    def qingqiu(self,page):
        # employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.86522508&x-zp-page-request-id=ba4169b228c54afab493b28e933d6fde-1573196958794-101796&x-zp-client-id=dadd826c-8aad-4163-a64d-59cb72ebc44b&MmEwMD=4GTdMwxd7dreVwOcscWBNCOI4e3mGOZKh8Pidlmxo4zCGQ4ZEcIpz_NRUDq.lmwzWBX8fqc1_xCGR6pa8CY4DoHqtu.LhXMwgEdsDAvY5hp6CXhEaYZD1GDZhKKuEwYyrBz4Gd21GXLFEaFn34oTxCc.RK1SZqfAZacJl4SDQZwknxf5alFzx3y82AU6oSsEklpa_ELoN2nptxSdkRrQOeUu.lzkZUd7lGzjsucd.8aIt63HFoHn5FzCo8uhJRZJXA0WgH5hKsew4SKyNperxAOp4VN_.hf0xYnjNnNW_HStpGIaYtEhoZwAvpiWwCvjhlUhnR3scKTUNem0vmRlt4J_HaurqzvR_O5prnxmqjOYlpcUBIVgs38NT8Q.OjpvMx530xSLd3wVOAdtMCl_NvTvTVSBAuUa7KldIYOCHDMVag1DMfAdt7B6PajAMr15qV8l'
        url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.86522508&x-zp-page-request-id=ba4169b228c54afab493b28e933d6fde-1573196958794-101796&x-zp-client-id=dadd826c-8aad-4163-a64d-59cb72ebc44b&MmEwMD=4l7ytyAyeM34my_lcbYNg1_RjRrkSo2AF_4EXGQHKI0aSgP_RbDUZ8aIDPRzYfl.wh63a9MV.zBbEsECH1WeUOKDMAt9HRcVkboxEKbyM.8bdGEnqldYKnaq60hhNtdaWm5qqekgngzUDqYByikFotq6iN7DGx.gg4Ug6HQbHqdI_6x4FL1BMciZ7fcQb1CGkQ8qYn7IOJJWngkb673KtkkBJ.z1Yn9ZZldCFBxkVxzihUO7i8fGWm4K9a5hMlcIJ5RGhfVxoxk535VclwtqDe_MX_Ai._Fb6tbt..u7C8uIbFg_WdPvsY.Cq7Ez7vwFno5Kc0FjqPDiz9_Hp1UFWs8apC39ut4q.847EPnyzCmYJjeNqqx4BLuhcXAvlOUvV8C0YKB9Itr9_ttYtMPdU52LTHqfwIiXa0_EIKf11d43LdKIlJDjU2ZS3a5ywmnzqSjv'.format(page)
        res = requests.get(url)
        html = res.json()
        return html

    def guo_lv(self,html):
        name,xinzi = [],[]
        for i in range(90):
            name_1 = html['data']['results'][i]['company']['name']
            xinzi_1 = html['data']['results'][i]['salary']
            name.append(name_1)
            xinzi.append(xinzi_1)
        shuju = dict(zip(name,xinzi))
        return shuju

    # def save_shuju(self,shuju):
    #     conn = pymysql.connect(host='192.168.10.98',port=3306,user='root',password='123456')
    #     su = conn.cursor()
    #     try:
    #         su.execute('create database zhilian;')
    #         su.execute('use zhilian;')
    #         su.execute('create table zhilian(name char(80),xinzi char(50));')
    #         for i,j in shuju.items():
    #             su.execute('insert into zhilian values("{}","{}");'.format(i,j))
    #             conn.commit()
    #     except:
    #         su.execute('use zhilian;')
    #         for i,j in shuju.items():
    #             su.execute('insert into zhilian values("{}","{}");'.format(i,j))
    #             conn.commit()
    #     finally:
    #         conn.close()
