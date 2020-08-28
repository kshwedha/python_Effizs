from cryptography import encrypt
from cryptography import decrypt

u_id={}
pwd={}
enc_p={}
key='bin!ris'

for i in range(10):
    username=raw_input("enter your username\n")
    passwd=raw_input("enter your password\n")
    username=str(username)
    passwd=str(passwd)
    e=encrypt(key,username)
    u_id[username]=e
    print(username +"\t"+ u_id[username])
    #print(username +"\t"+ repr(e))

    #ctypes.cast(address, ctypes.py_object).value
    #address=id(0xb754nf68)
    #if u_id=encrypt(key,x)
    #result would be
    #enter your username
    #"maath"
    #maath   <function encrypt at 0x7fbcf22d4dd0>

    enc_p[e]=passwd
    print(u_id[username] +"\t"+ enc_p[e])
    pwd[passwd]=username
    print(enc_p[e] +"\t"+ pwd[passwd])
