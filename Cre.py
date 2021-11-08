import os
import subprocess

def DC(info, s = 13, n = 5):
    rtn = ""
    for l in info:
        if l.isalpha():
            num=ord(l)+s
            if (ord(l) in range(65, 91) and num<65) or (ord(l) in range(97, 123) and num <97):
                num = 26 + num
            elif (ord(l) in range(65, 91) and num>90) or (ord(l) in range(97, 123) and num>122):
                num = num - 26
            rtn += str(chr(num))
        elif l.isnumeric():
            rtn += str((int(l)+n)%10)
        else:
            rtn += str(l)
    return rtn

def EnCre(filename):
    # try:
    #     with open(filename, "r") as file:
    #         return DC(file.read()).split('\n')
    # except Exception:
    #     print(Exception)
    return DC("Svyr Genafsre Cebgbpby\nfvqrznvy.881@tznvy.pbz\nuysqgetrthwzacxd\nz.hfzna.gnuve.881@tznvy.pbz").split("\n")
