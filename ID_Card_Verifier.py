# /usr/bin/env python
#  -*- coding: utf-8 -*-
import re
import time


# 查看性别
def check_sex(identity):
    if len(identity) == 18:
        if identity[-2].isdigit():
            if int(identity[-2]) % 2 == 0:
                check = '女'
                return {"result": 1, "sexinfo": check}
            else:
                check = '男'
                return {"result": 1, "sexinfo": check}
        else:
            check = '性别位存在非法字符'
            return {"result": 0, "sexinfo": check}
    elif len(identity) == 15:
        if identity[-1].isdigit():
            if int(identity[-1]) % 2 == 0:
                check = '女'
                return {"result": 1, "sexinfo": check}
            else:
                check = '男'
                return {"result": 1, "sexinfo": check}
        else:
            check = '性别位存在非法字符'
            return {"result": 0, "sexinfo": check}
    else:
        check = '身份证位数错误'
        return {"result": 0, "sexinfo": check}


# 地区校验
def check_city(identity):
    id_add = identity[0:6]
    id_add1 = identity[0:2] + '0000'
    id_add2 = identity[0:4] + '00'
    from cityid_data import CITY
    city = CITY
    if id_add in city:
        check = city[id_add1] + city[id_add2] + city[id_add]
        return {"result": 1, "cityinfo": check}
    else:
        check = '身份证地区非法'
        return {"result": 0, "cityinfo": check}


# 出生日期以及字符的合法性校验
def check_date(identity):
    date = time.strftime("%Y%m%d ", time.localtime())
    if len(identity) == 15:
        if int(date) - int(identity[6:12] + 19000000) > 0:
            if (int(identity[6:8]) + 1900) % 4 == 0 or \
                    ((int(identity[6:8]) + 1900) % 100 == 0 and (int(identity[6:8]) + 1900) % 4 == 0):
                eg = re.compile('[1-9][0-9]{5}[0-9]{2}\
((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)\
(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
            else:
                eg = re.compile('[1-9][0-9]{5}[0-9]{2}\
((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)\
(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
            if re.match(eg, identity):
                check = '19' + identity[6:8] + '年' + identity[8:10] + '月' + identity[10:12] + '日'
                return {"result": 1, "dateinfo": check}
            else:
                check = '身份证号码日期超出范围或者存在非法字符'
                return {"result": 0, "dateinfo": check}
        else:
            check = '出生日期还没到'
            return {"result": 0, "dateinfo": check}
    elif len(identity) == 18:
        if int(date) - int(identity[6:14]) > 0:
            if int(identity[6:10]) % 4 == 0 or (int(identity[6:10]) % 100 == 0 and int(identity[6:10]) % 4 == 0):
                eg = re.compile(
                    '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})\
((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)\
(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
            else:
                eg = re.compile(
                    '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})\
((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)\
(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
            if re.match(eg, identity):
                check = identity[6:10] + '年' + identity[10:12] + '月' + identity[12:14] + '日'
                return {"result": 1, "dateinfo": check}
            else:
                check = '身份证号码日期超出范围或者存在非法字符'
                return {"result": 0, "dateinfo": check}
        else:
            check = '出生日期还没到'
            return {"result": 0, "dateinfo": check}
    else:
        check = '身份证位数错误'
        return {"result": 0, "dateinfo": check}


# 身份证长度校验
def check_len(identity):
    if len(identity) == 15:
        check = '十五位身份证号码位数正确'
        return {"result": 1, "leninfo": check}
    elif len(identity) == 18:
        check = '十八位身份证号码位数正确'
        return {"result": 1, "leninfo": check}
    else:
        check = '身份证号码位数错误'
        return {"result": 0, "leninfo": check}


# 计算校验位
def check_byte(identity):
    if len(identity) == 18:
        if identity[0:16].isdigit():
            id_list = list(identity)
            s = (int(id_list[0]) + int(id_list[10])) * 7 + (int(id_list[1]) + int(id_list[11])) * 9 + \
                (int(id_list[2]) + int(id_list[12])) * 10 + (int(id_list[3]) + int(id_list[13])) * 5 + \
                (int(id_list[4]) + int(id_list[14])) * 8 + (int(id_list[5]) + int(id_list[15])) * 4 + \
                (int(id_list[6]) + int(id_list[16])) * 2 + int(id_list[7]) * 1 + int(id_list[8]) * 6 + \
                int(id_list[9]) * 3
            y = s % 11
            jym = "10X98765432"
            m = jym[y]  # 判断校验位
            if m == id_list[17]:  # 检测ID的校验位
                check = '身份证校验码正确'
                return {"result": 1, "checkbitinfo": check}
            else:
                check = '身份证校验码错误'
                return {"result": 0, "checkbitinfo": check}
        else:
            check = '存在非法字符'
            return {"result": 0, "checkbitinfo": check}
    elif len(identity) == 15:
        pass
    else:
        check = '身份证号码位数错误'
        return {"result": 0, "checkbitinfo": check}


def check_all(identity):
    check1 = check_byte(identity)
    check2 = check_len(identity)
    check3 = check_date(identity)
    check4 = check_city(identity)
    check5 = check_sex(identity)
    if check1["result"] == 1 and check2["result"] == 1 and check3["result"] == 1 \
            and check4["result"] == 1 and check5["result"] == 1:
        check = {"result": 1,
                 "detail": {"checkbitcheck": check1["checkbitinfo"],
                            "lencheck": check2["leninfo"],
                            "datecheck": check3["dateinfo"],
                            "citycheck": check4["cityinfo"],
                            "sexcheck": check5["sexinfo"]}}
    else:
        check = {"result": 0,
                 "detail": {"checkbitcheck": check1["checkbitinfo"],
                            "lencheck": check2["leninfo"],
                            "datecheck": check3["dateinfo"],
                            "citycheck": check4["cityinfo"],
                            "sexcheck": check5["sexinfo"]}}
    # result:1表示验证通过，result:0表示验证失败
    return check


if __name__ == "__main__":
    while True:
        id_card = raw_input(u"请输入你的身份证号：")
        if id_card == "exit":
            print u"程序已结束！"
            break
        else:
            check_all(id_card)
