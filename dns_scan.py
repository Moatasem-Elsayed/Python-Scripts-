from dns.rdatatype import NULL
import dns.resolver
import socket

Types=["A","AAA","MX","NS","SOA","SRV","CNAME"]

ip=socket.gethostbyname(socket.gethostname())
for targe in Types:
    try:
        d = dns.resolver.query("google.com",targe,raise_on_no_answer=False)
        if (d.rrset != None):
            print (d.rrset)

    except:
        pass