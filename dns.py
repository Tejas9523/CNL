import socket

while 1:
    print("1.IP to URL")
    print("2.URL to IP")
    print("3.EXIT")
    n = int(input("Enter choice : "))
    if n == 1:
        ip = input("Enter IP : ")
        domain = socket.gethostbyaddr(ip)
        print(domain)
    elif n == 2:
        add = input("Enter URL : ")
        ip = socket.gethostbyname(add)
        print(ip)
    else:
        0
