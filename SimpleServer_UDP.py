import socket 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=socket.gethostbyname(socket.gethostname())
print("your ip is : "+ip)

print("=============================")
s.bind((ip,5000))
while True :
    rodata,address=s.recvfrom(1024)
    print(f"{address} is sending to you this message {rodata.decode('UTF-8')}")

    print("=============================")
    msg=str(input("please enter the message that you want to send: "))
    msg_encoded=msg.encode('UTF-8')
    s.sendto(msg_encoded,address)