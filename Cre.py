import string
import random

def DC(info, s = 13, n = 5):
    """[File Encryptor/Decryptor]

    Args:
        info ([string]): [The data to be encrypted or decrypted]
        s (int, optional): [The decipher key to string characters in data]. Defaults to 13.
        n (int, optional): [The decipher key to int characters in data]. Defaults to 5.

    Returns:
        [string]: [The data after encryption or decryption]
    """
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

def PasswordGenerator():
    Password = ""
    Rand = string.ascii_letters+string.digits
    for i in range(8):
        Password += random.choice(Rand)
    return Password

if __name__ == '__main__':
    PasswordGenerator()