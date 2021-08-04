import socket
import pyautogui
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip_address = socket.gethostbyname(socket.gethostname())
    s.bind(("127.0.0.1",8888))
    s.listen(5)
    client,addr=s.accept()
    print(addr[0])
    while(True):
        data=client.recv(5000)
        print(data.decode("utf-8"))
        command=str(input("< command >"))
        client.send(command.encode("utf-8"))
except socket.error as e:
    print(e)
    
s.close()