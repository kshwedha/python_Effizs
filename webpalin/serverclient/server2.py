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
        while True:
            data = conn.recv(4096)
            if not data: break
            from_client += data
            print from_client
            conn.send("I am SERVER\n")
    else:
        conn.send("password wrong...")
    conn.close()
    print 'client disconnected'
