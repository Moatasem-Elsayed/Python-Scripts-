import socket
try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    portlist=[22,80,443]
    #sock.settimeout(10)
    ip=socket.gethostbyname("www.google.com")
    for i in portlist:
        scan=sock.connect_ex((ip,i))
        if scan == 0:
            print("{} is openned : Service {}".format(i,socket.getservbyport(i)))
        else:
            print("{} is Closed : Service {}".format(i,socket.getservbyport(i)))
except socket.error as e:
    print(e)