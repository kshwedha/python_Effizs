import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8080))
serv.listen(60)

while True:
    conn, addr = serv.accept()
    from_client = ''
    pin="maath26"
    conn.send("enter the login pin....")
    passwd=conn.recv(4096)
    if passwd==pin:
        conn.send("I am the SERVER\n")
        who_data=conn.recv(32)
        print(who_data)
        while True:
            send_data=input("S:")
            if send_data is chr(126): #or send_data is not type(str):
                conn.close()
                break
            else:
                conn.send(send_data)
                data = conn.recv(4096)
                if not data: break
                #from_client += data
                from_client=data
                print("C:"+from_client)
    else:
        conn.send("password wrong...")
        conn.close()
        print 'client disconnected'
conn.close()
