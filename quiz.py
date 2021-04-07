import socket 

def Socket_ClientSend(name,id,score,server):  
    # Create a socket object 
    s = socket.socket()         
    
    # Define the port on which you want to connect 
    port = 3333                
    
    # connect to the server on local computer 
    s.connect((server, port)) 
    
    # receive data from the server
    formstring=f"{id}:{name}  Score => {score}" 
    s.sendall(formstring.encode('ascii'))
    print (s.recv(3000) )
    # close the connection 
    s.close()

print("****** Welcome Our Student Please Solve First Quiz *******")
print("*** Please Active CapsLock To Select Capital Letter  *******") 
print(" ")
name=input("Name: ")
ID=input("ID: ")
Server=input("Server: ")
print(" ")
Q1=input("C Programming is faster than Cpp ? ( T ),( F )")
print(" ")
Q2=input("bitmask means changing in bits without effect on any bit else ? ( T ),( F )")
print(" ")
Q3=input("Gcc is compiler for c and g++ for cpp ? ( T ),( F )")
print(" ")
Q4=input("c89 ,c99,c11 are standards for C programming  ( T ),( F )")
print(" ")
Q5=input("char is one byte and behave like signed char -127 to 128 ? ( T ),( F )")
print(" ")
Q6=input("Float is larger than double ? ( T ),( F )")
print(" ")
Q7=input("int is 4 byte forever  ? ( T ),( F )")
print(" ")
Q8=input("char x=128; so x will be ? ? ( -128 ),( 128 )")
print(" ")
Q9=input("printf(hello) will print hello ? ( T ),( F )")
print(" ")
Q10=input("C is created for unix kernal  ? ( T ),( F )")
print(" ")

Y=0
Truelist=[Q1,Q2,Q3,Q4,Q5,Q10]
FalseList=[Q6,Q7,Q9]

for x in Truelist:
    if x == "T" or  x =="t":
        Y+=1     

for x in FalseList:
    if x == "F"  or x=='f':
        Y+=1     
if Q8 == '-128':
    Y+=1 

print(f"Your Score is : {Y}/10")
input("******* Please Click Enter To Close *********")
Socket_ClientSend(name.capitalize(),ID.strip(),Y,Server.strip())
# Import socket module 
            
            




