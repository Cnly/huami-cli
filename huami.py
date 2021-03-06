#!/usr/bin/env python
# coding=utf8
# Huami CLI Version.
# Author: Tao Yang (ninehills.github.com)
# Origin: https://code.google.com/p/flower-password/
# Usage: huami.py [KEY]
import sys
import hmac

STR1 = "snow"
STR2 = "kise"
STR3 = "sunlovesnow1990090127xykab"


def huami(password, key):
    """计算花密密码
    """
    # 得到md5one, md5two, md5three
    # hmac.new(key, msg)
    md5one = hmac.new(key, password).hexdigest()
    md5two = hmac.new(STR1, md5one).hexdigest()
    md5three = hmac.new(STR2, md5one).hexdigest()
    # 转换大小写
    rule = list(md5three)
    source = list(md5two)
    for i in range(0, 32):
        if rule[i] in STR3:
            source[i] = source[i].upper()
    #code32 = ''.join(source)
    #保证密码首字母为字母---why?
    if source[0].isdigit():
        code16 = "K" + "".join(source[1:16])
    else:
        code16 = "".join(source[0:16])
    return code16

if __name__ == "__main__":

    import getpass
    password = getpass.getpass("Password:")

    if len(sys.argv) != 2:
        key = raw_input('Key:')
    else:
        key = sys.argv[1]

    print huami(password, key)
