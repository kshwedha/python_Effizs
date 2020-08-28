#msg='hello_world this is my personnal'
#key="this_is_my_key"

def encrypt(key,msg):
    encryped=[]
    for i, c in enumerate(msg):
        key_c=ord(key[i%len(key)])
        #print(key_c)
        #it prints the ascii value of key characters
        msg_c=ord(c)
        #hello world this is my personnal.
        #this_is_my_keythis_is_my_keythis_
        encryped.append(chr((msg_c+key_c)%127))
        #print((msg_c+key_c)%127)
        #print(encryped[i])
    return ''.join(encryped)

def decrypt(key, encryped):
    msg=[]
    for i, c in enumerate(encryped):
        key_c=ord(key[i%len(key)])
        enc_c=ord(c)
        #print(enc_c)
        msg.append(chr((enc_c-key_c)%127))
    return ''.join(msg)

if __name__=='__main__':
    encrypted=encrypt(key, msg)
    decrypted=decrypt(key, encrypted)

    print 'Message:', repr(msg)
    print 'Key:', repr(key)
    print 'Encrypted:', repr(encrypted)
    print 'Decrypted:', repr(decrypted)

