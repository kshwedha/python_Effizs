import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

data=client.recv(4096)
print(data+"\n")
pin=input()
client.send(pin)
verify_data=client.recv(64)
if verify_data=="password wrong...":
    print(verify_data+"\n")
    client.close()
else:
    print(verify_data)
    client.send("I am CLIENT\n")
    x=True
    while True==x:
        from_server=client.recv(4096)
        print("S:"+from_server)
        sdata = input("C:")
        if sdata is chr(126): #or sdata is not type(str):
            client.close()
            x=False
            break
        else:
            client.send(sdata)



