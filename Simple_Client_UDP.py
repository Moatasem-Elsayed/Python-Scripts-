import socket 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=socket.gethostbyname(socket.gethostname())
print("your ip is : "+ip)
print("=============================")
while True:
    msg=str(input("please enter the message that you want to send: "))
    msg_encoded=msg.encode('UTF-8')
    s.sendto(msg_encoded,(ip,5000))

    print("=============================")
    rodata,address=s.recvfrom(1024)
    print(f"{address} is sending to you this message {rodata.decode('UTF-8')}")

