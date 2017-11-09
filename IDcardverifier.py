# /usr/bin/env python
#  -*- coding: utf-8 -*-
import re
import pickle

pickle_file = open('cityid_data.pkl', 'rb')
city = pickle.load(pickle_file)

# Errors=['验证通过!','身份证号码位数不对!','身份证号码出生日期超出范围或含有非法字符!','身份证号码校验错误!','身份证地区非法!']
def checkIdcard(idcard):
    Errors = ['验证通过!', '身份证号码位数不对!', '身份证号码出生日期超出范围或含有非法字符!', '身份证号码校验错误!', '身份证地区非法!']
    area = city
    idcard = str(idcard)
    idcard = idcard.strip()
    idcard_list = list(idcard)

    # 地区校验
    if (not (idcard)[0:6] in area):
        print Errors[4]
        if __name__ == "__main__":
            while True:
                cdcard = raw_input(u"请输入你的身份证号：")
                if cdcard == "exit":
                    print u"程序已结束！"
                    break
                else:
                    checkIdcard(cdcard)
    # 15位身份号码检测
    if (len(idcard) == 15):
        if ((int(idcard[6:8]) + 1900) % 4 == 0 or ((int(idcard[6:8]) + 1900) % 100 == 0 and (int(idcard[6:8]) + 1900) % 4 == 0)):
            ereg = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
        else:
            ereg = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
        if (re.match(ereg, idcard)):
            print Errors[0]
            ID_add = idcard[0:6]
            ID_add1 = idcard[0:2] + '0000'
            ID_add2 = idcard[0:4] + '00'
            ID_sex = idcard[-1]
            ID_birth = idcard[6:12]
            year = ID_birth[0:2]
            moon = ID_birth[2:4]
            day = ID_birth[4:6]
            print("发证地区: " + area[ID_add1] + area[ID_add2] + area[ID_add])
            print("出生日期: 19" + year + '年' + moon + '月' + day + '日')
            if int(ID_sex) % 2 == 0:
                print('性别：女')
            else:
                print('性别：男')
        else:
            print Errors[2]
    # 18位身份号码检测
    elif (len(idcard) == 18):
        # 出生日期的合法性检查
        # 闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
        # 平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
        if (int(idcard[6:10]) % 4 == 0 or (int(idcard[6:10]) % 100 == 0 and int(idcard[6:10]) % 4 == 0)):
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
        else:
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
        # //测试出生日期的合法性
        if (re.match(ereg, idcard)):
            # //计算校验位
            S = (int(idcard_list[0]) + int(idcard_list[10])) * 7 + (int(idcard_list[1]) + int(idcard_list[11])) * 9 + \
                (int(idcard_list[2]) + int(idcard_list[12])) * 10 + (int(idcard_list[3]) + int(idcard_list[13])) * 5 + \
                (int(idcard_list[4]) + int(idcard_list[14])) * 8 + (int(idcard_list[5]) + int(idcard_list[15])) * 4 + \
                (int(idcard_list[6]) + int(idcard_list[16])) * 2 + int(idcard_list[7]) * 1 + int(idcard_list[8]) * 6 + int(idcard_list[9]) * 3
            Y = S % 11
            M = "F"
            JYM = "10X98765432"
            M = JYM[Y]  # 判断校验位
            if (M == idcard_list[17]):  # 检测ID的校验位
                print Errors[0]
                ID_add = idcard[0:6]
                ID_add1 = idcard[0:2] + '0000'
                ID_add2 = idcard[0:4] + '00'
                ID_sex = idcard[-2]
                ID_birth = idcard[6:14]
                year = ID_birth[0:4]
                moon = ID_birth[4:6]
                day = ID_birth[6:8]
                print("发证地区: " + area[ID_add1] + area[ID_add2] + area[ID_add])
                print("出生日期: " + year + '年' + moon + '月' + day + '日')
                if int(ID_sex) % 2 == 0:
                    print('性别：女')
                else:
                    print('性别：男')
            else:
                print Errors[3]
        else:
            print Errors[2]
    else:
        print Errors[1]


if __name__ == "__main__":
    while True:
        cdcard = raw_input(u"请输入你的身份证号：")
        if cdcard == "exit":
            print u"程序已结束！"
            break
        else:
            checkIdcard(cdcard)
