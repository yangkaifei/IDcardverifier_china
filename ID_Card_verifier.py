# /usr/bin/env python
#  -*- coding: utf-8 -*-
import re
import pickle

# 查看性别
def checkSex(ID):
    if len(ID) == 18:
        if int(ID[-2]) % 2 == 0:
            check = '女'
        else:
            check = '男'
    elif len(ID)  == 15:
        if int(ID[-1]) %2 == 0:
            check = '女'
        else:
            check = '男'
    return check  

# 地区校验
def checkCity(ID):
    ID_add = ID[0:6]
    ID_add1 = ID[0:2] + '0000'
    ID_add2 = ID[0:4] + '00'
    pickle_file = open('cityid_data.pkl', 'rb')
    city = pickle.load(pickle_file)
    if ID_add in city:
        check = '发证地区：' + city[ID_add1] + city[ID_add2] + city[ID_add]
    else:
        check = '身份证地区非法'
    return check

# 出生日期以及字符的合法性校验
def checkDate(ID):
    if (len(ID) == 15):
        if ((int(ID[6:8]) + 1900) % 4 == 0 or ((int(ID[6:8]) + 1900) % 100 == 0 and (int(ID[6:8]) + 1900) % 4 == 0)):
            ereg = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
        else:
            ereg = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
        if (re.match(ereg, ID)):
            check = '出生日期:19' + ID[6:8] + '年' + ID[8:10] + '月' + ID[10:12] + '日'
        else:
            check = '身份证号码日期超出范围或者存在非法字符'
    elif (len(ID) == 18):
        if (int(ID[6:10]) % 4 == 0 or (int(ID[6:10]) % 100 == 0 and int(ID[6:10]) % 4 == 0)):
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
        else:
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
        if (re.match(ereg, ID)):
            check = '出生日期:' + ID[6:10] + '年' + ID[10:12] + '月' + ID[12:14] + '日'
        else:
            check = '身份证号码日期超出范围或者存在非法字符'
    return check

#身份证长度校验
def checkLen(ID):
    if (len(ID) != 15 or 18):
         check = '身份证号码位数不对'
    return check

# 计算校验位
def checkByte(ID):
    if (len(ID) == 18):
      ID_list = list(ID)
      S = (int(ID_list[0]) + int(ID_list[10])) * 7 + (int(ID_list[1]) + int(ID_list[11])) * 9 + \
            (int(ID_list[2]) + int(ID_list[12])) * 10 + (int(ID_list[3]) + int(ID_list[13])) * 5 + \
            (int(ID_list[4]) + int(ID_list[14])) * 8 + (int(ID_list[5]) + int(ID_list[15])) * 4 + \
            (int(ID_list[6]) + int(ID_list[16])) * 2 + int(ID_list[7]) * 1 + int(ID_list[8]) * 6 + int(ID_list[9]) * 3
      Y = S % 11
      M = "F"
      JYM = "10X98765432"
      M = JYM[Y]  # 判断校验位
      if (M == ID_list[17]):  # 检测ID的校验位
        check = '身份证校验正确'
      else:
        check = '身份证校验错误'
      return check








